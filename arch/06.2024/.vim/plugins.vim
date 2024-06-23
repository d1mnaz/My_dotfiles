vim9script


# -----------------------------AutoInstall VimPlug------------------------------
 g:need_to_install_plugins = 0
 if empty(glob('~/.vim/autoload/plug.vim'))
     silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
         \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
     g:need_to_install_plugins = 1
 endif



# ---------------------------------List plugins---------------------------------
plug#begin()
    Plug 'Eliot00/auto-pairs'
    Plug 'alvan/vim-closetag'
    Plug 'airblade/vim-gitgutter'
    Plug 'mbbill/undotree'
    Plug 'tpope/vim-commentary'
    Plug 'machakann/vim-sandwich'
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'
    Plug 'ap/vim-css-color'
    Plug 'dense-analysis/ale'
plug#end()



#---------------------------------Vim-closetag----------------------------------

# Настройки для vim-closetag для jsx
g:closetag_filenames = '*.html,*.tsx,*.jsx,*.js,*.ts'

# make sure it only works for the JSX region
g:closetag_regions = {
     'typescript.tsx': 'jsxRegion,tsxRegion',
     'javascript.jsx': 'jsxRegion',
     }


# -------------------------------------ALE--------------------------------------

# Цвета
highlight clear ALEErrorSign
highlight clear ALEWarningSign


# Автокомлит (0 = false, 1 = true)
g:ale_completion_enabled = 0
set omnifunc=ale#completion#OmniFunc


# Настройки линтеров
g:ale_linters = {'jsx': ['tsserver', 'eslint'], 'astro': ['eslint'], 'tsx': ['tsserver', ], }
g:ale_linter_aliases = {'jsx': ['css', 'javascript'], 'tsx': ['tsserver'], }

g:ale_linters_ignore = { 'python': ['pylint', 'mypy', 'flake8'], }
g:ale_linters = { 'python': ['ruff', 'pyright' ], }

g:ale_fixers = { '*': ['remove_trailing_lines', 'trim_whitespace'], 
	'python': ['black'], 
	'javascript': ['prettier'], 
	'javascript.jsx': ['prettier'], 
	'typescript': ['prettier'], 
	'typescriptreact': ['prettier'], }
g:ale_linter_aliases = {'typescriptreact': 'typescript'}


g:ale_set_highlights = 1
g:ale_virtualtext_cursor = 0
g:ale_echo_msg_format = '[%linter%] %s [%severity%] %code%'
g:ale_floating_preview = 1
g:ale_set_quickfix = 0
g:ale_floating_window_border = []

# отключение при наборе и фикс при сохранении файла
g:ale_lint_on_insert_leave = 1
# g:ale_lint_on_text_changed = 'never'
g:ale_fix_on_save = 1
