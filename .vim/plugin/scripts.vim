" очистка регистра
command! WipeReg for i in range(34,122) | silent! call setreg(nr2char(i), []) | endfor

function! XTermPasteBegin()
    set pastetoggle=<Esc>[201~
    set paste
    return ""
endfunction

inoremap <special> <expr> <Esc>[200~ XTermPasteBegin()

" Filter the quickfix list
function! FilterQFList(type, action, pattern)
    " get current quickfix list
    let s:curList = getqflist()
    let s:newList = []
    for item in s:curList
        if a:type == 0     " filter on file names
            let s:cmpPat = bufname(item.bufnr)
        elseif a:type == 1 " filter by line content
            let s:cmpPat = item.text . item.pattern
        endif
        if item.valid
            if a:action < 0
                " Keep only nonmatching lines
                if s:cmpPat !~ a:pattern
                    let s:newList += [item]
                endif
            else
                " Keep only matching lines
                if s:cmpPat =~ a:pattern
                    let s:newList += [item]
                endif
            endif
        endif
    endfor
    call setqflist(s:newList)
endfunction

nnoremap <leader>z :call FilterQFList(0, -1, inputdialog('Remove file names matching:', ''))<CR>
nnoremap <leader>a :call FilterQFList(0, 1, inputdialog('Keep only file names matching:', ''))<CR>
nnoremap <leader>aa :call FilterQFList(1, -1, inputdialog('Remove all lines matching:', ''))<CR>
nnoremap <leader>zz :call FilterQFList(1, 1, inputdialog('Keep only lines matching:', ''))<CR>

" FancySmancyComment(text, fill_char, width)
" Create comment string with centered text
" All arguments are optional
function! FancySmancyComment(...)
  let text = get(a:000, 0, '')
  let fill = get(a:000, 1, '-')[0]
  let width = get(a:000, 2, 80) - len(printf(&commentstring, '')) - len(text)
  let left = width / 2
  let right = width - left
  put=printf(&commentstring, repeat(fill, left) . text . repeat(fill, right))
endfunction
command! -nargs=1 Fancy call FancySmancyComment(<q-args>)

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

"----------------------------------LSP server-----------------------------------

let lspServers = [
\     #{
\    filetype: ['javascript', 'typescript', 'javascriptreact', 'typescriptreact',],
\    path: '/usr/lib/node_modules/typescript-language-server/lib/cli.js',
\    args: ['--stdio']
\      },
\      #{
\   filetype: ['javascript', 'typescript'],
\   path: '/usr/bin/typescript-language-server',
\   args: ['--stdio']
\      },
\     #{
\    filetype: ['python'],
\    path: '/usr/bin/pylsp',
\    args: []
\      },
\     #{
\    filetype: 'vim',
\    path: '/usr/bin/vim-language-server',
\    args: ['--stdio']
\      },
\   ]

autocmd VimEnter * call LspAddServer(lspServers)
let lspOpts = {'autoHighlightDiags': v:true,
      \'autoComplete': v:false,
      \'showDiagOnStatusLine': v:true,
      \'noNewlineInCompletion': v:true,
      \'outlineOnRight': v:true
      \}
autocmd VimEnter * call LspOptionsSet(lspOpts)


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
" set grepprg=rg\ --vimgrep\ --follow\ --max-columns=500\ -i

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
let g:fzf_tags_command = 'ctags -R'
" Border color
let g:fzf_layout = {'up':'~90%', 'window': { 'width': 0.8, 'height': 0.8,'yoffset':0.5,'xoffset': 0.5, 'highlight': 'Todo', 'border': 'sharp' } }
" let g:fzf_layout = { 'window': 'vs' } " in case preview not working properly.
let $FZF_DEFAULT_OPTS = '--layout=reverse --info=inline' "might add --no-unicode
let $FZF_DEFAULT_COMMAND="rg --files --hidden"
