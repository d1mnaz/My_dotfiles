vim9script

# _____________Color Themes__________
set termguicolors                  # Use true colors.
colorscheme akaruy
set background=light

# Включаем 256 цветов в терминале
set t_Co=256

# Меняет линию курсора при наборе
autocmd InsertEnter * highlight CursorLine guifg=NONE guibg=#edfff1
autocmd InsertLeave * highlight CursorLine guifg=NONE guibg=#f0f0f0

