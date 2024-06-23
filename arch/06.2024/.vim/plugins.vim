vim9script
# plugins
 g:need_to_install_plugins = 0
 if empty(glob('~/.vim/autoload/plug.vim'))
     silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
         \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
     g:need_to_install_plugins = 1
 endif

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
plug#end()



#---------------------------------Vim-closetag----------------------------------
# Настройки для vim-closetag для jsx
# add file extensions
g:closetag_filenames = '*.html,*.tsx,*.jsx,*.js,*.ts'

# make sure it only works for the JSX region
g:closetag_regions = {
     'typescript.tsx': 'jsxRegion,tsxRegion',
     'javascript.jsx': 'jsxRegion',
     }
