#!/bin/bash
export DISPLAY=:0
xhost +
setterm -blank 0
setterm -powersave off
xset -dpms

date >> /tmp/monitor

function kill_stuff() {
    for var in chrome google-chrome python node nodejs screen
    do
	killall $var 2>/dev/null
	sleep .25
	killall $var 2>/dev/null
	sleep .25
	killall -9 $var 2>/dev/null
    done
}

kill_stuff

python ~/dimo-control/control.py

# launch input
cd ~/dimo-input
python server.py &

# launch browser
google-chrome file:///home/dimo/current_demo/index.html &
