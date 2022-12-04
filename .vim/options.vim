vim9script

#   Автоматически создать директорию undo для восстановления файлов
if !isdirectory($HOME .. "/.vim/undo")
    mkdir($HOME .. "/.vim/undo", "p", 0o755)
endif

# настройка satstusLine
set laststatus=2
set statusline=
set statusline+=\%#Terminal#
set statusline+=%2*[%n%M%H%R%W]%\*
set statusline+=\%#DiffDelete#
# set statusline+=%#Visual#
set statusline+=%f
set statusline+=\%#Terminal#
set statusline+=%=
set statusline+=\ %y
set statusline+=\ %p%%
set statusline+=\ %#CursorColumn#
set statusline+=\ %l:%c
set statusline+=
set statusline+=\ 

# Включить подсветку синтаксиса
syntax on

# Определение типа файла и отступов
filetype plugin indent on

# Кодировка файлов по умолчанию
set encoding=utf-8
set fileformat=unix
set fileencoding=utf-8

# Кодировка терминала
set termencoding=utf-8

# Переносим на другую строчку, разрываем строки
# set wrap
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

set tabstop=2
set shiftwidth=2
set smarttab
set expandtab # Ставим табы пробелами
set softtabstop=2

# Автоотступ
set autoindent

set nu # Включаем нумерацию строк
set mousehide # Спрятать курсор мыши когда набираем текст
set mouse=a # Включить поддержку мыши


set shell=zsh
set shellcmdflag=-c
set colorcolumn=80

set updatetime=300
set scrolloff=10

set clipboard+=unnamedplus

set nobackup
set noswapfile
set undofile
set undoreload=10000
set undodir=~/.vim/undo

# history / file handling
set history=999
set undolevels=999

# reload files if changed externally
set autoread

# Change directory to the current buffer when opening files.
# set autowriteall
# set autowrite

set ttyfast
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

# Настройка для тегов
set tags=.tags
set tags+=~/Projects/askarate.moscow/backend/.tags
set tags+=~/Projects/askarate.moscow/frontend/.tags
set tagcase=match
set matchpairs+=<:>,「:」

set foldmethod=manual
set foldlevel=99

set langmap=ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯЖ;ABCDEFGHIJKLMNOPQRSTUVWXYZ:,фисвуапршолдьтщзйкыегмцчня;abcdefghijklmnopqrstuvwxyz

# -------------Search-------------- #
set path+=**5
set path+=~/Projects/askarate.moscow/backend/**
set path+=~/Projects/askarate.moscow/frontend/**
set hlsearch
set incsearch
set ignorecase
set smartcase
set wildignorecase
set wildignore+=**/node_modules/**
set wildignore+=**/venv/**,**/coverage/**
set wildignore+=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx
set wildignore+=*.git/*,*.tags,tags,*.o,*.class,*.ccls-cache
set splitbelow
set splitright


# disable autoindent when pasting text
# source: https://coderwall.com/p/if9mda/automatically-set-paste-mode-in-vim-when-pasting-in-insert-mode
&t_SI = "\<Esc>[?2004h"
&t_EI = "\<Esc>[?2004l"


#_____________NetRw File explorer__________#

# g:netrw_list_hide = netrw_gitignore#Hide()
g:netrw_list_hide = '.*\.swp$,.DS_Store,*/tmp/*,*.so,*.swp,*.zip,*.git,*.o,*.pyc,^\.\.\=/\=$,.idea,.git,__pycache__,.mypy_cache,.pytest_cache,venv,node_modules'
g:netrw_keepdir = 0
g:netrw_banner = 0
g:netrw_localcopydircmd = 'cp -r'



# использовать ripgrep при поиске слова
set grepprg=rg\ --vimgrep\ --smart-case\ --hidden\ --follow\ --max-columns=500\ -i
set grepformat=%f:%l:%c:%m

set completeopt=menuone,noselect       # Insert mode completion:
                                       # menuone   → always show menu, even when there is 1 match.
                                       # noselect  → don't select an option when starting.
set completepopup=highlight:Pmenu,border:off  # Options for preview popup in completion.
set pumheight=20                       # Don't make completion menu too high.


set omnifunc=LspOmniFunc

# Diffs are shown side-by-side not above/below
set diffopt=vertical
# Always show the sign column
set signcolumn=no
