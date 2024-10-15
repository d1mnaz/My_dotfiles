source /home/dimon/.local/share/zsh/antigen.zsh
antigen use oh-my-zsh
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-autosuggestions
antigen bundle zsh-users/zsh-completions
antigen bundle git
antigen theme robbyrussell
antigen apply
ZSH_THEME="robbyrussell"
TERM=xterm-256color
export EDITOR=vim
export PATH="$PATH:/home/dimon/.cargo/bin"
export PATH="$PATH:/home/dimon/.local/bin"
autoload -U colors && colors
export LS_COLORS
# fix background color dirs from ls
LS_COLORS+=':ow=01;32'
ColorOff='\\\e[0m'       # Text Reset
BWhite='\\\e[1;37m'      # Bold White

#_____________________Alias________________________________________#

alias myip="curl http://ipecho.net/plain; echo"
alias rm='nocorrect rm -Irv'
alias mkdir='nocorrect mkdir'
alias kd='asus-kbd-backlight 0'
alias exx='extract'
alias rr='sudo reboot'
alias ro='sudo poweroff'
alias h=history
alias grep='rg'
alias lt='tree -IC __pycache__'
alias cv='vim ~/.vimrc'
alias pwgen='pwgen -csn1 32'
alias dusort='du -s *|sort -nr|cut -f 2-|while read a;do du -hs $a;done'
alias sv='source venv/bin/activate'
alias p='python3.12'
alias g='git'
alias ptp='ptpython'
alias tl='tldr'
alias tn='tmux new -s'
# alias tmux='tmux -2'
alias tmux="TERM=screen-256color tmux -2"
alias vi='vim'
alias up='sudo wg-quick up wg0'
alias down='sudo wg-quick down wg0'
alias led='ledger -f ~/Documents/Pip-Boy/led.dat'
alias ledadd='vim ~/Documents/Pip-Boy/led.dat'
alias work='sudo ntfs-3g /dev/nvd0p2 /mnt/Work'
# alias mpv='smplayer'
alias copy='rsync -a --info=progress2'
alias w3m='w3m -cols 80'
alias mtl=' ~/.dict/mueller-base.sh'


alias pi='sudo pkg install --yes'
alias pr='sudo pkg remove'
alias pu='sudo pkg update && sudo pkg upgrade'
alias pks='pkg search'

# alias -g -- -h='-h 2>&1 | bat --language=help --style=plain'
# alias -g -- --help='--help 2>&1 | bat --language=help --style=plain'
# alias bat='bat --theme=TwoDark --color=always'


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


export FZF_DEFAULT_COMMAND="fd . $HOME"
export FZF_DEFAULT_COMMAND="fd --exclude={.git,.idea,.vscode,.sass-cache,node_modules,build} --type f . $HOME"

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



[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

python_venv() {
  MYVENV=./venv
  # when you cd into a folder that contains $MYVENV
  [[ -d $MYVENV ]] && source $MYVENV/bin/activate > /dev/null 2>&1
  # when you cd into a folder that doesn't
  # [[ ! -d $MYVENV ]] && deactivate > /dev/null 2>&1
}
autoload -U add-zsh-hook
add-zsh-hook chpwd python_venv

python_venv

