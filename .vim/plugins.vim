vim9script

# plugins
# g:need_to_install_plugins = 0
# if empty(glob('~/.vim/autoload/plug.vim'))
#     silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
#         \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
#     g:need_to_install_plugins = 1
# endif
#
plug#begin()
    Plug 'Eliot00/auto-pairs'
    Plug 'alvan/vim-closetag'
    Plug 'airblade/vim-gitgutter'
    Plug 'yegappan/lsp'
    Plug 'mbbill/undotree'
    Plug 'ap/vim-css-color'
    Plug 'tpope/vim-commentary'
    Plug 'machakann/vim-sandwich'
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'
    Plug 'sheerun/vim-polyglot'
plug#end()


#---------------------------------Vim-closetag----------------------------------
# Настройки для vim-closetag для jsx
# add file extensions
g:closetag_filenames = '*.html,*.tsx,*.jsx'

# make sure it only works for the JSX region
g:closetag_regions = {
     'typescript.tsx': 'jsxRegion,tsxRegion',
     'javascript.jsx': 'jsxRegion',
     }


#-------------------------------Vim9-fuzzy plugin-------------------------------
# Enable vim9-fuzzy
packadd! vim9-fuzzy
var proj_dir = getcwd()
var git_root = system("git rev-parse --show-toplevel | tr -d '\n'")
if len(git_root) > 0
    proj_dir = git_root
endif
g:vim9_fuzzy_proj_dir = proj_dir


