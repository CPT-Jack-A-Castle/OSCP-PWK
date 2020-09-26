# OSCP
### Notes and cheetsheets are in Wiki pages. Repo is mostly filled with writeups and binaries.

# TryHackMe
### Most of the writeups are for THM

# Kali Config
ohmyzsh + powerlevel10K + tmux

### font
1. Goto `~/.config/qterminal.org` folder
2. Change fontFamily to Fira Code or somethingelse and save exit.
3. All set, remember don't use Qterminal to do the above steps, otherwise changes wont take place. Use editor directlry open file instead.
4. Should all working now. Either use mate-terminal or do it with GUI editor. 

### .zshrc
`unsetopt PROMPT_SP` remove the %(percent sign) when starting a terminal

`alias tmux='TERM=xterm-256color tmux -2'` make tmux support 256 color
