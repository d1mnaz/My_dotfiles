vim9script

#   Автоматически создать директорию undo для восстановления файлов
if !isdirectory($HOME .. "/.cache/vim/undo")
    !mkdir($HOME .. "/.cache/vim/undo", "p", 0o755)
endif


# настройка satstusLine {{{
set laststatus=2
set statusline=
set statusline+=\%#CursorColumn#
set statusline+=%2*[%n%M%h%R%W]%\*
set statusline+=\%#CursorColumn#
# set statusline+=\%#DiffDelete#
# set statusline+=%#Visual#
set statusline+=%f
set statusline+=\%#CursorColumn#
set statusline+=%=
set statusline+=\ %p%%
set statusline+=\ %l:%c
set statusline+=
set statusline+=\ %#CursorColumn#
set statusline+=\ %y
# }}}

# Включить подсветку синтаксиса
syntax on

# Определение типа файла и отступов
filetype plugin indent on

# Отключить перенос строк
set nowrap
set linebreak

# Вырубаем черточки на табах
set showtabline=1
# Удобное поведение backspace
set backspace=indent,eol,start whichwrap+=<,>,[,]

# Всегда показывать текущую позицию
set ruler

# Переключается между буферами без вопросов о сохранении
set hidden

# Автоотступ
set autoindent

set nu # Включаем нумерацию строк
set mousehide # Спрятать курсор мыши когда набираем текст
set scrolloff=10
set nobackup
set noswapfile
set undofile
set undoreload=10000
# reload files if changed externally
set autoread

# Change directory to the current buffer when opening files.
set autowriteall
set autowrite
set showmode
set showcmd
# Вертикальное меню
set wildmenu
set wildoptions=pum
set wildoptions+=fuzzy
# Use list mode and customized listchars
set list listchars=tab:▸\ ,extends:❯,precedes:❮,nbsp:+,trail:·,nbsp:·


# Changing fillchars for folding, so there is no garbage charactes
set fillchars=fold:\ ,vert:\|
set foldmethod=manual
set foldlevel=99
set langmap=ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯЖ;ABCDEFGHIJKLMNOPQRSTUVWXYZ:,фисвуапршолдьтщзйкыегмцчня;abcdefghijklmnopqrstuvwxyz
# -------------Search-------------- {{{
set path+=**5
set hlsearch
set incsearch
set ignorecase
set smartcase
set wildignorecase
set wildignore+=**/node_modules/**
set wildignore+=**/venv/**,**/coverage/**
set wildignore+=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx
set wildignore+=*.git/*,*.tags,tags,*.o,*.class,*.ccls-cache
# }}}

# Открывать новое окно всегда снизу или справа
set splitbelow
set splitright
#_____________NetRw File explorer__________#

# g:netrw_list_hide = netrw_gitignore#Hide()
g:netrw_list_hide = '.*\.swp$,.DS_Store,*/tmp/*,*.so,*.swp,*.zip,*.git,*.o,*.pyc,^\.\.\=/\=$,.idea,.git,__pycache__,.mypy_cache,.pytest_cache,venv,node_modules'
g:netrw_keepdir = 1
g:netrw_banner = 0
g:netrw_localcopydircmd = 'cp -r'



# использовать ripgrep при поиске слова
set grepprg=rg\ --vimgrep\ --smart-case\ --hidden\ --follow\ --max-columns=500\ -i
set grepformat=%f:%l:%c:%m
set completeopt=menuone,noselect       # Insert mode completion:
                                       # menuone   → always show menu, even when there is 1 match.
                                       # noselect  → don't select an option when starting.
set completepopup=highlight:Visual,border:off  # Options for preview popup in completion.
set pumheight=20                       # Don't make completion menu too high.
# Diffs are shown side-by-side not above/below
set diffopt=vertical
