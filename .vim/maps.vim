vim9script

#-------------Mappings--------------#

# Редактирование Vimrc file в новом табе
map <Leader>ev :tabedit $MYVIMRC<cr>

# Add simple highlight removal.
nmap <silent> <BS> :nohlsearch<CR>

# Переключения по буфферам
noremap <C-Right> :bn<CR>
noremap <C-Left> :bp<CR>
noremap <S-l> :bn<CR>
noremap <S-h> :bp<CR>
nmap <S-q> :bp<bar>bd#<CR>
nnoremap <Leader>bb :buffers<CR>:buffer<Space>
nmap <leader>x :.+,$bw<CR>

# Разделение окна
nmap ss :split<CR>
nmap sv :vsplit<CR>

# Алиас для быстрой замены в файле
nnoremap S :%s//g<Left><Left>

nnoremap k gk
nnoremap j gj
map 0 ^


# Перемещение по окну исправлений
nnoremap <silent> <leader>] :cnext <CR>
nnoremap <silent> <leader>[ :cprevious <CR>

# Копирование в системный буфер
noremap <S-Y> "+y

# When completion menu is shown, use <cr> to select an item
# and do not add an annoying newline. Otherwise, <enter> is what it is.
# For more info , see https://superuser.com/q/246641/736190 and
# https://unix.stackexchange.com/q/162528/221410
inoremap <expr> <cr> ((pumvisible()) ? ("\<C-Y>") : ("\<cr>"))
# Use <esc> to close auto-completion menu
inoremap <expr> <esc> ((pumvisible()) ? ("\<C-e>") : ("\<esc>"))

# Use <tab> to navigate down the completion menu.
inoremap <expr> <tab>  pumvisible() ? "\<C-n>" : "\<tab>"

# Поиск слова из функции Better Grep в scripts
nmap <leader>gg :Grep<space><space>.<left><left>
nmap gw :GrepWord<space><c-r><c-w><space>.<cr>

# Hit enter in the file browser to open the selected
noremap  <C-E> :Explore %:p:h<CR>

# Run make
nnoremap <leader>l :make %<cr>:copen<cr>:redraw!<cr>

# Регулирование размеров вертикального окна
nnoremap + :vert res +5<CR>
nnoremap _ :vert res -5<CR>

# Позволяет разбивать текущую сторку на несколько для отображения
noremap <silent> <Leader>w :call ToggleWrap()<CR>


# Открывает или закрывает окно QuickFix
nnoremap <leader>q :call ToggleQuickFix()<cr>


# _________________Map for plugins__________________________


# Поиск fzf  с плагином Vim9FuzzyFile
# Search by only file name.
noremap <C-f> :Vim9FuzzyFile<CR>
# Search by full path
noremap <C-p> :Vim9FuzzyPath<CR>


# Поиск слова по всей текущей директории plugin fzf
nmap <leader>g :Rg<space><cr>
nmap <leader>b :Buffers<space><cr>
nnoremap <leader>G :GFiles<CR>

# поиск файлов
nmap <leader>f :Files<space><cr>

# Открыть окно просмотра версий файла (нужен плагин Undotree)
nnoremap <F8> :UndotreeToggle<CR>


# Для Lsp servera
nnoremap <leader>da : call LspOptionsSet({'autoComplete': v:true})<cr>:LspServerRestart<cr>
nnoremap <leader>dd : call LspOptionsSet({'autoComplete': v:false })<cr>:LspServerRestart<cr>

nnoremap <silent> <C-k> :LspDiagCurrent<cr>
nnoremap <silent> <C-h> :LspHover<cr>
nnoremap <silent> <C-l> :LspDiagShow<cr>
nnoremap <silent> <C-d> :LspGotoDefinition<CR>
nnoremap <leader>gd :LspGotoDeclaration<cr>
nnoremap <silent> <F9> :LspOutline<cr>
nnoremap <leader>dh :LspHover<cr>
nnoremap <leader>dn :LspDiagNext<cr>
nnoremap <leader>dp :LspDiagPrev<cr>
nnoremap <leader>df :LspReferences<cr>
nnoremap <leader>dr :LspRename<cr>
