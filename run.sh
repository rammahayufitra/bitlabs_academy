#!/bin/sh 
xhost +local:
docker run --rm --privileged -it --net=host  -e DISPLAY=$DISPLAY -v ~/bitlabs_academy:/app -v /tmp/.X11-unix:/tmp/.X11-unix bitlabs_academy bash