vim9script

#-------------Auto-Commands--------------#


# Изменить клавиши перемещения в Netrw (файловом браузере)
def NetrwMapping()
    nmap <buffer> H u
    nmap <buffer> h -^
    nmap <buffer> l <CR>
    setlocal statusline=\ %f
enddef

# Запустить функцию для перемещения в файловом браузере
augroup Netrwoptions | autocmd!
    autocmd filetype netrw call NetrwMapping()
    # Quit Vim if Netrw is the only window
    autocmd WinEnter * if winnr('$') == 1 && getbufvar(winbufnr(winnr()), "&filetype") == "netrw"|q|endif
augroup end

# Восстанавливает положение курсора из прошлой сессии
autocmd BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

# CursorLine current window
augroup CursorLine
    au!
    au VimEnter,WinEnter,BufWinEnter * setlocal cursorline
    au WinLeave * setlocal nocursorline
augroup END

# Меняет линию курсора при наборе
autocmd InsertEnter * highlight CursorLine guifg=NONE guibg=#edfff1
autocmd InsertLeave * highlight CursorLine guifg=NONE guibg=#f0f0f0

# Восстанавливать складки
augroup Remember_folds
  autocmd!
  autocmd BufWinLeave *.* mkview
  autocmd BufWinEnter *.* silent! loadview
augroup END


# Автозакрытие окна при автокомплите
augroup Completion_preview_close
  autocmd!
  autocmd CompleteDone * if !&previewwindow && &completeopt =~ 'preview' | silent! pclose | endif
augroup END

# Сохранять измененный буфер во время простоя по истечении 'updatetime' (по умолчанию 4 сек.)
autocmd CursorHoldI,CursorHold * silent! update
