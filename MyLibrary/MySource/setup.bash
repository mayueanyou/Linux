#!/usr/bin/env sh

work_dir=$(dirname "$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)")

export PATH=$PATH:"$work_dir"/MyFunction
export PYTHONPATH=$PYTHONPATH:"$work_dir"/Ros
source "$work_dir"/MySource/ros.bash

#source /home/my/MyLibrary/MySource/miniconda2.bash
#source /home/my/MyLibrary/MySource/miniconda3.bash
