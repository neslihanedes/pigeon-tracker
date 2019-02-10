#!/usr/bin/env bash

docker run -it \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    -v $(pwd):/pigeon-tracker \
    -u $(id -u ${USER}):$(id -g ${USER}) \
    --workdir /pigeon-tracker \
    pigeon-tracker \
    bash
