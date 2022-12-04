vim9script

# _____________Color Themes__________


if $TERM =~ '256color'
    set termguicolors                  # Use true colors.
    &t_8f = "\<Esc>[38;2;%lu;%lu;%lum" # Set correct escape codes to make termguicolors work in st.
    &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
    &t_SI = "\<Esc>[5 q"               # Start Insert; set cursor to underline (1=block, 3=underline, 5=bar).
    &t_SR = &t_SI                      # Start Replace.
    &t_EI = "\<Esc>[1 q"               # End Insert (or Replace), set back to block cursor.
endif

colorscheme akaruy
set background=light

# Включаем 256 цветов в терминале
set t_Co=256

highlight Comment cterm=italic
highlight htmlArg cterm=italic
highlight MatchParen guibg='#fde5f1' guifg='#4B3D44'
# highlight Identifier  guifg='#2a7bde'
autocmd InsertEnter * highlight CursorLine guifg=NONE guibg=#f1edff
autocmd InsertLeave * highlight CursorLine guifg=NONE guibg=#f0f0f0

# Синтаксис для Python из плагина python-syntax
g:python_highlight_all = 1
