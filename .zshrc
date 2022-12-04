#Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh
export LDFLAGS="-rdynamic"
autoload -U compinit promptinit
# compinit
# promptinit; prompt gentoo


#PROMPT='%f%F{blue}%f%b%(!.#.$) '
#RPROMPT="%{$fg_bold[grey]%}%~/%{$reset_color%}%"
export MANOPT="-L ru"
export PATH="$PATH:/home/dimon/.cargo/bin"
export PATH="$PATH:/home/dimon/.local/bin"
# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
ZSH_THEME="robbyrussell"
# [ -n "$PS1" ] && sh ~/.vim/plugged/cosmic_latte/shell/cosmic_latte_dark.sh
autoload -U colors && colors
# Base16 Shell
#BASE16_SHELL="$HOME/.config/base16-shell/base16-material.dark.sh"
#[[ -s $BASE16_SHELL ]] && source $BASE16_SHELL
TERM=xterm-256color
#export LS_COLORS='no=00;95:fi=00;37:di=01;36:ln=04;36:pi=33:so=01;35:do=01;35:bd=33;01:cd=33;01:or=31;01:su=45:sg=30:tw=30:ow=34:st=90:ex=01;31:'
#LS_COLORS='di=1:fi=0:ln=31:pi=5:so=5:bd=5:cd=5:or=31:mi=0:ex=35:*.rpm=92'
export LS_COLORS
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
#export VISUAL="vim"
export EDITOR=vim
bindkey -v
# fix background color dirs from ls
LS_COLORS+=':ow=01;32'


#_____________________Alias________________________________________#

alias myip="curl http://ipecho.net/plain; echo"
alias sudo='nocorrect sudo'
alias exx='extract'
alias rr='sudo reboot -i'
alias ro='sudo poweroff'
alias h=history
alias grep='ripgrep'
alias ls='lsd -I __pycache__'
alias ll='lsd -l'
alias la='lsd -a'
alias lla='ls -la'
alias lt='lsd --tree --depth'
alias pb='cd /run/media/dimon/Work/PipBoy'
# alias ls='ls --classify --color=auto --human-readable --group-directories-first'
# alias ls='ls --group-directories-first  --color=auto -F' 
alias cp='nocorrect cp --interactive --verbose --recursive --preserve=all'
alias mv='nocorrect mv --verbose --interactive'
alias rm='nocorrect rm -Irv'
alias mkdir='nocorrect mkdir'
alias kd='asus-kbd-backlight 0'
alias man='man -L ru'
alias -g M='| more'G
alias -g L='| less'
alias -g H='| head'
alias -g T='| tail'
alias -g G="| grep"
alias mtl=' ~/.dict/mueller-base.sh'
alias ca='vim ~/.config/awesome/rc.lua'
alias cv='vim ~/.vimrc'
alias mtp='jmtpfs ~/.mtp'
alias umtp='fusermount -u ~/.mtp'
alias cm='unimatrix -c blue'
alias pwgen='pwgen -csn1 32'
alias jn='jupyter-lab'
alias gt='LANG=en_US.UTF-8 gtypist -c 0,7 -S'
alias dusort='du -s *|sort -nr|cut -f 2-|while read a;do du -hs $a;done'
alias sv='source venv/bin/activate'
alias cdc='cd /run/media/dimon/Work/code'
alias p='python'
alias g='git'
alias ptp='ptpython'
alias tl='tldr'
alias tn='tmux new -s'
alias tmux='tmux -2'
alias vi='nvim'
alias lint='isort . && flake8 . && black .'
alias up='sudo wg-quick up wg0'
alias down='sudo wg-quick down wg0'
alias ncdu='ncdu --color off'
alias running='systemctl --type=service --state=running'
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
# Uncomment the following line to use case-sensitive completion.

# CASE_SENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to disable command auto-correction.
# DISABLE_CORRECTION="true"


# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
plugins=( zsh-z)

source $ZSH/oh-my-zsh.sh

# User configuration

# export PATH="/usr/local/sbin:/usr/local/bin:/usr/bin:/opt/kde/bin:/usr/bin/core_perl:/home/dimon/.local/bin:/home/dimon/.cargo/bin"
# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"



ColorOff='\\\e[0m'       # Text Reset
BWhite='\\\e[1;37m'      # Bold White
#source /etc/zsh_command_not_found
#
#
alias -s {avi,mp4}="mpv"
alias -s {jpg,png}="feh"
alias -s {pdf,djvu}="evince"
echo -e `curl -s  fucking-great-advice.ru/api/random | awk -F \" '{print $6}'` |sed 's/\&nbsp;/ /g'

name() {
    name=$1
    vared -c -p 'rename to: ' name
    command mv $1 $name
} 
extract () {
 if [ -f $1 ] ; then
 case $1 in
 *.tar.bz2)   tar xjf $1        ;;
 *.tar.gz)    tar xzf $1     ;;
 *.bz2)       bunzip2 $1       ;;
 *.rar)       unrar x $1     ;;
 *.gz)        gunzip $1     ;;
 *.tar)       tar xf $1        ;;
 *.tbz2)      tar xjf $1      ;;
 *.tgz)       tar xzf $1       ;;
 *.zip)       unzip $1     ;;
 *.Z)         uncompress $1  ;;
 *.7z)        7z x $1    ;;
 *.tbz)       tar xjvf  ;;
 *)           echo "я не в курсе как распаковать '$1'..." ;;
 esac
 else
 echo "'$1' is not a valid file"
 fi
} 

# упаковка в архив
pk () {
 if [ $1 ] ; then
 case $1 in
 tbz)       tar cjvf $2.tar.bz2 $2      ;;
 tgz)       tar czvf $2.tar.gz  $2       ;;
 tar)      tar cpvf $2.tar  $2       ;;
 bz2)    bzip $2 ;;
 gz)        gzip -c -9 -n $2 > $2.gz ;;
 zip)       zip -r $2.zip $2   ;;
 7z)        7z a $2.7z $2    ;;
 *)         echo "'$1' cannot be packed via pk()" ;;
 esac
 else
 echo "'$1' is not a valid file"
 fi

}
#source /usr/share/doc/pkgfile/command-not-found.zsh
# ssh
# export SSH_KEY_PATH="~/.ssh/dsa_id"


#Virtualenv
#export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
#source /usr/bin/virtualenvwrapper.sh
# eval $(dircolors -b $HOME/.dircolors)
function exists { which $1 &> /dev/null }

# if exists percol; then
#     function percol_select_history() {
#         local tac
#         exists gtac && tac="gtac" || { exists tac && tac="tac" || { tac="tail -r" } }
#         BUFFER=$(fc -l -n 1 | eval $tac | percol --query "$LBUFFER")
#         CURSOR=$#BUFFER         # move cursor
#         zle -R -c               # refresh
#     }

#     zle -N percol_select_history
#     bindkey '^R' percol_select_history
# fi
# source /home/dimon/.config/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

source /usr/share/fzf/key-bindings.zsh
source /usr/share/fzf/completion.zsh



#[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

#eval "dircolors /path/to/dircolorsdb"
export BAT_THEME="ansi"

# the detailed meaning of the below three variable can be found in `man zshparam`.
export HISTFILE=~/.zsh_history
export HISTSIZE=1000000   # the number of items for the internal history list
export SAVEHIST=1000000   # maximum number of items for the history file

# The meaning of these options can be found in man page of `zshoptions`.
setopt HIST_IGNORE_ALL_DUPS  # do not put duplicated command into history list
setopt HIST_SAVE_NO_DUPS  # do not save duplicated command
setopt HIST_REDUCE_BLANKS  # remove unnecessary blanks
setopt INC_APPEND_HISTORY_TIME  # append command to history file immediately after execution
setopt EXTENDED_HISTORY  # record command start time
zstyle ':completion::complete:*' use-cache 1
# fix background color dirs from ls
LS_COLORS+=':ow=01;32'


setopt inc_append_history
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_find_no_dups
setopt hist_ignore_space
setopt hist_reduce_blanks

# [ -z "$NVM_DIR" ] && export NVM_DIR="$HOME/.nvm"
# source /usr/share/nvm/nvm.sh
# source /usr/share/nvm/bash_completion
# source /usr/share/nvm/install-nvm-exec

export FZF_DEFAULT_COMMAND="fd . $HOME"
export FZF_DEFAULT_COMMAND="fd --exclude={.git,.idea,.vscode,.sass-cache,node_modules,build} --type f . $HOME"

unsetopt nomatch
setopt noglob
vim='noglob vim'
