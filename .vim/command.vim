vim9script

#-------------Auto-Commands--------------#

# Automatically source the Vimrc file on save.
augroup autosourcing
  autocmd!
  autocmd BufWritePost .vimrc source %
augroup END

# Изменить клавиши перемещения в Netrw (файловом браузере)
def NetrwMapping()
    nmap <buffer> H u
    nmap <buffer> h -^
    nmap <buffer> l <CR>
enddef

# Запустить функцию для перемещения в файловом браузере
augroup Netrw_mapping
    autocmd!
    autocmd filetype netrw NetrwMapping()
augroup END

# Восстанавливает положение курсора из прошлой сессии
autocmd BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

# use syntax for omnicomplete if none exists
# augroup SyntaxComplete
#     autocmd Filetype * if &omnifunc == '' | setlocal omnifunc=syntaxcomplete#Complete | endif
# augroup end

# CursorLine current window
augroup CursorLine
    au!
    au VimEnter,WinEnter,BufWinEnter * setlocal cursorline
    au WinLeave * setlocal nocursorline
augroup END

# Save with root permission
command! W w !sudo tee > /dev/null %

# ctags generations
command! MakeTags !ctags -R -f .tags .

# More accurate syntax highlighting? (see `:h syn-sync`)
augroup accurate_syn_highlight
    autocmd!
    autocmd BufEnter * :syntax sync fromstart
augroup END

# Настройки для JavaScriptReact
augroup JavascriptReact
    autocmd!
    autocmd FileType  javascriptreact,typescriptreact autocmd BufWritePre <buffer> :%s/\($\n\s*\)\+\%$//e
    autocmd BufWritePre *.js,*.jsx,*.ts,*.tsx :LspFormat
augroup END

# Настройки для Python
augroup Python
    autocmd!
    autocmd FileType python setlocal tabstop=4
    autocmd FileType python setlocal softtabstop=4
    autocmd FileType python setlocal shiftwidth=4
    # Run Python
    autocmd Filetype python nnoremap <buffer> <F6> :w<CR>:vert ter ++cols=50 python3 "%"<CR>
    autocmd Filetype python nnoremap <buffer> <F5> :w<CR>:!python3 "%"<CR>
  autocmd FileType python autocmd BufWritePre <buffer> :%s/\($\n\s*\)\+\%$//e
    autocmd BufWritePre *.py :LspFormat
augroup END


# Восстанавливать складки
augroup remember_folds
  autocmd!
  autocmd BufWinLeave *.* mkview
  autocmd BufWinEnter *.* silent! loadview
augroup END

# Автозакрытие окна при автокомплите
augroup completion_preview_close
  autocmd!
  autocmd CompleteDone * if !&previewwindow && &completeopt =~ 'preview' | silent! pclose | endif
augroup END
