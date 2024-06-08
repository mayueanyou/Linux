# Linux


## nautilus-terminal

https://github.com/flozz/nautilus-terminal#nautilus-terminal-doesnt-show-up

## ssh

https://www.ssh.com/academy/ssh/keygen

### none-passwd login

`ssh-keygen -t ecdsa -b 521`

`ssh-copy-id -i ~/.ssh/key user@host`

## chrome remote desktop
restart the service

`systemctl restart chrome-remote-desktop@`

## system monitor

`sudo apt-get install nmon`

`sudo nmon`


## Tips

### use vnc remote desktop

https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04

### update the default terminal

`sudo update-alternatives --config x-terminal-emulator`

### waydroid

#### Install Instructions

https://docs.waydro.id/usage/install-on-desktops

`waydroid init -s GAPPS`

#### Install weston

`sudo apt install weston`

#### Google Play Certification

https://docs.waydro.id/faq/google-play-certification 
