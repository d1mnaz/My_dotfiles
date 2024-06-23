vim9script


#   Автоматически создать директорию undo для восстановления файлов
for item in [&undodir, &viewdir ]
    if !isdirectory(expand(item))
	 mkdir(expand(item), 'p')
    endif
endfor

set nobackup
set noswapfile
set undoreload=10000
set undofile
set viewdir=~/.vim/.state/view
set undodir=~/.vim/.state/undo
set viminfofile=~/.vim/.state/viminfo
set notimeout ttimeout ttimeoutlen=0




# ------------------------Настройки  Statusline------------------------

set laststatus=2
set statusline=
set statusline+=\%#SignColumn#
set statusline+=🐼
set statusline+=%2*[%n%M%h%R%W]%\*
set statusline+=\%#Cursor#
set statusline+=%f
set statusline+=\%#Cursor#
set statusline+=%=
set statusline+=\ %p%%
set statusline+=\ %l:%c
set statusline+=
set statusline+=\ %#Cursor#
set statusline+=\ %y

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


# ---------------------------Настройки  Tab----------------------------
set tabstop=2
set shiftwidth=2
set smarttab
set expandtab # Ставим табы пробелами
set softtabstop=2

set nu # Включаем нумерацию строк
set mousehide # Спрятать курсор мыши когда набираем текст
set scrolloff=10

# Открывать новое окно всегда снизу или справа
set splitbelow
set splitright

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



# ---------------------Настройки для поиск---------------------
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


# --------------------------Настройки  Netrw---------------------------
g:netrw_list_hide = '.*\.swp$,.DS_Store,*/tmp/*,*.so,*.swp,*.zip,*.git,*.o,*.pyc,^\.\.\=/\=$,.idea,.git,__pycache__,.mypy_cache,.pytest_cache,venv,node_modules'
g:netrw_keepdir = 1
g:netrw_banner = 0
g:netrw_localcopydircmd = 'cp -r'


# использовать ripgrep при поиске слова
set grepprg=rg\ --vimgrep\ --smart-case\ --hidden\ --follow\ --max-columns=500\ -i
set grepformat=%f:%l:%c:%m

# Insert mode completion:
# menuone   → always show menu, even when there is 1 match.
# noselect  → don't select an option when starting.
set completeopt=menuone,noselect
set completepopup=highlight:Visual,border:off  # Options for preview popup in completion.
set pumheight=20                       # Don't make completion menu too high.

# Diffs are shown side-by-side not above/below
set diffopt=vertical
