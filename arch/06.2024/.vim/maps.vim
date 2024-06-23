vim9script


# -----------------------------------Mappings-----------------------------------

# Редактирование Vimrc file в новом табе
map <Leader>ev :tabedit $MYVIMRC<cr>

# Add simple highlight removal.
nmap <silent> <BS> :nohlsearch<CR>

# Переключения по буфферам
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

# Копирование в системный буфер
noremap <S-Y> "+y

# Hit enter in the file browser to open the selected
noremap  <C-E> :Explore %:p:h<CR>



# -------------------Для меню автокомплита-------------------

# When completion menu is shown, use <cr> to select an item
inoremap <expr> <cr> ((pumvisible()) ? ("\<C-Y>") : ("\<cr>"))
# Use <esc> to close auto-completion menu
inoremap <expr> <esc> ((pumvisible()) ? ("\<C-e>") : ("\<esc>"))
# Use <tab> to navigate down the completion menu.
inoremap <expr> <tab>  pumvisible() ? "\<C-n>" : "\<tab>"



# -------------------------------Map for function from script-------------------------------

# Позволяет разбивать текущую сторку на несколько для отображения
noremap <silent> <Leader>w :call ToggleWrap()<CR>


# Поиск слова из функции Better Grep в scripts
nmap <leader>gg :Grep<space><space>.<left><left>

# Поиск слова  под курсором из функции Better Grep в scripts
nmap gw :GrepWord<space><c-r><c-w><space>.<cr>

# Открывает или закрывает окно QuickFix
nnoremap <leader>q :call ToggleQuickFix()<cr>


# Включает автодополнение по относительному пути к файлам
inoremap <C-x><C-x><C-f> <C-o>:call <SID>EnableRelativeAutocomplete()<CR><C-x><C-f>


# Отображает атрибуты подсветки синтаксиса символа под курсором;
map -a :call SyntaxAttr()<CR>

# -------------------------------Map for plugins--------------------------------

# Поиск fzf
nmap <leader>g :Rg<space><cr>
nmap <leader>b :Buffers<space><cr>
nnoremap <leader>G :GFiles<CR>
nmap <leader>f :Files<space><cr>

# Открыть окно просмотра версий файла (нужен плагин Undotree)
nnoremap <F8> :UndotreeToggle<CR>


#  Hotkeys for ALE
nmap <leader>a :ALEToggle<CR>
nmap <silent> <C-k> <Plug>(ale_previous_wrap)
nmap <silent> <C-j> <Plug>(ale_next_wrap)
nmap <silent> gh <Plug>(ale_hover)
nmap <silent> <C-d> <Plug>(ale_go_to_definition)
nmap <silent> gr <Plug>(ale_find_references)
