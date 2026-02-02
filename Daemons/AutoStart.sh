#!/bin/bash
picom --daemon --config ~/.config/picom/picom.conf &
pulseaudio --start &
numlockx on &
redshift -O 4000