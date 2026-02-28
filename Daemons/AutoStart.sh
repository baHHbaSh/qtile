#!/bin/bash
picom --daemon --config ~/.config/picom/picom.conf &
pulseaudio --start &
numlockx on &
copyq &
redshift -O 4000