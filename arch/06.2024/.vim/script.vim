
"----------------------------------ToggleWrap-----------------------------------
function ToggleWrap()
    if &wrap
        echo "Wrap OFF"
        setlocal nowrap
        set virtualedit=all
        silent! nunmap <buffer> <Up>
        silent! nunmap <buffer> <Down>
        silent! nunmap <buffer> <Home>
        silent! nunmap <buffer> <End>
        silent! iunmap <buffer> <Up>
        silent! iunmap <buffer> <Down>
        silent! iunmap <buffer> <Home>
        silent! iunmap <buffer> <End>
    else
        echo "Wrap ON"
        setlocal wrap linebreak nolist
        set virtualedit=
        setlocal display+=lastline
        noremap  <buffer> <silent> <Up>   gk
        noremap  <buffer> <silent> <Down> gj
        noremap  <buffer> <silent> <Home> g<Home>
        noremap  <buffer> <silent> <End>  g<End>
        inoremap <buffer> <silent> <Up>   <C-o>gk
        inoremap <buffer> <silent> <Down> <C-o>gj
        inoremap <buffer> <silent> <Home> <C-o>g<Home>
        inoremap <buffer> <silent> <End>  <C-o>g<End>
    endif
endfunction

"----------------------------------Better Grep----------------------------------

function! Grep(...)
    let s:command = join([&grepprg] + [expandcmd(join(a:000, ' '))], ' ')
    return system(s:command)
endfunction

command! -nargs=+ -complete=file_in_path -bar Grep  cgetexpr Grep(<f-args>)
command! -nargs=+ -complete=file_in_path -bar GrepWord  cgetexpr Grep(<f-args> . ' -w')

cnoreabbrev <expr> grep  (getcmdtype() ==# ':' && getcmdline() ==# 'grep')  ? 'Grep'  : 'grep'

augroup quickfix
    autocmd!
    autocmd QuickFixCmdPost cgetexpr cwindow
                \| call setqflist([], 'a', {'title': ':' . s:command})
augroup END

"----------------------------------FZF plugin-----------------------------------
command! -bang -nargs=? -complete=dir Files
    \ call fzf#vim#files(<q-args>, fzf#vim#with_preview(), <bang>0)
command! -bang -nargs=? -complete=dir GFiles
    \ call fzf#vim#gitfiles(<q-args>, fzf#vim#with_preview(), <bang>0)
command! -bang -nargs=* Rg
    \ call fzf#vim#grep(
    \   'rg --column --line-number --no-heading --color=always --smart-case -- '.shellescape(<q-args>), 1,
    \   fzf#vim#with_preview(), <bang>0)

" Border color
let g:fzf_layout = {'up':'~90%', 'window': { 'width': 0.8, 'height': 0.8,'yoffset':0.5,'xoffset': 0.5, 'highlight': 'Todo', 'border': 'sharp' } }
let $FZF_DEFAULT_OPTS = '--layout=reverse --info=inline' "might add --no-unicode
let $FZF_DEFAULT_COMMAND="rg --files --hidden"


" Открывает окно справки справа
if has('autocmd')
  function! ILikeHelpToTheRight()
    if !exists('w:help_is_moved') || w:help_is_moved != "right"
      wincmd L
      let w:help_is_moved = "right"
    endif
  endfunction

  augroup HelpPages
    autocmd FileType help nested call ILikeHelpToTheRight()
  augroup END
endif

" buffers and quickfix
function! ToggleQuickFix()
  if empty(filter(getwininfo(), 'v:val.quickfix'))
    copen
  else
    cclose
  endif
endfunction

" project root finder
function! Rooter() abort
    " https://vi.stackexchange.com/questions/20605/find-project-root-relative-to-the-active-buffer/20606
    let l:dir=finddir('.git/..', expand('%:p:h').';')
    echom 'cwd: ' . l:dir
    execute 'silent lcd ' . l:dir
endfunction

command! Rooter call Rooter()


" Отображает атрибуты подсветки синтаксиса символа под курсором; 
function! SyntaxAttr()
     let synid = ""
     let guifg = ""
     let guibg = ""
     let gui   = ""

     let id1  = synID(line("."), col("."), 1)
     let tid1 = synIDtrans(id1)

     if synIDattr(id1, "name") != ""
	  let synid = "group: " . synIDattr(id1, "name")
	  if (tid1 != id1)
	       let synid = synid . '->' . synIDattr(tid1, "name")
	  endif
	  let id0 = synID(line("."), col("."), 0)
	  if (synIDattr(id1, "name") != synIDattr(id0, "name"))
	       let synid = synid .  " (" . synIDattr(id0, "name")
	       let tid0 = synIDtrans(id0)
	       if (tid0 != id0)
		    let synid = synid . '->' . synIDattr(tid0, "name")
	       endif
	       let synid = synid . ")"
	  endif
     endif

     " Use the translated id for all the color & attribute lookups; the linked id yields blank values.
     if (synIDattr(tid1, "fg") != "" )
	  let guifg = " guifg=" . synIDattr(tid1, "fg") . "(" . synIDattr(tid1, "fg#") . ")"
     endif
     if (synIDattr(tid1, "bg") != "" )
	  let guibg = " guibg=" . synIDattr(tid1, "bg") . "(" . synIDattr(tid1, "bg#") . ")"
     endif
     if (synIDattr(tid1, "bold"     ))
	  let gui   = gui . ",bold"
     endif
     if (synIDattr(tid1, "italic"   ))
	  let gui   = gui . ",italic"
     endif
     if (synIDattr(tid1, "reverse"  ))
	  let gui   = gui . ",reverse"
     endif
     if (synIDattr(tid1, "inverse"  ))
	  let gui   = gui . ",inverse"
     endif
     if (synIDattr(tid1, "underline"))
	  let gui   = gui . ",underline"
     endif
     if (gui != ""                  )
	  let gui   = substitute(gui, "^,", " gui=", "")
     endif

     echohl MoreMsg
     let message = synid . guifg . guibg . gui
     if message == ""
	  echohl WarningMsg
	  let message = "<no syntax group here>"
     endif
     echo message
     echohl None
endfunction
map -a :call SyntaxAttr()<CR>

"------------------------------RelativAutocomplet-------------------------------
function! s:EnableRelativeAutocomplete() abort
  let b:relative_autocomplete_cleanup_pending = 1
  lcd %:p:h
endfunction

function! s:DisableRelativeAutocomplete() abort
  if exists('b:relative_autocomplete_cleanup_pending') && b:relative_autocomplete_cleanup_pending
    lcd -
    let b:relative_autocomplete_cleanup_pending = 0
  endif
endfunction


augroup relative_file_autocomplete
  autocmd!
  autocmd InsertLeave * call s:DisableRelativeAutocomplete()
augroup END

" Включает автодополнение по относительному пути к файлам
inoremap <C-x><C-x><C-f> <C-o>:call <SID>EnableRelativeAutocomplete()<CR><C-x><C-f>
