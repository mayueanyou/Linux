#!/usr/bin/env bash

work_dir=$(dirname "$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)")

export PATH=$PATH:"$work_dir"/MyFunction
#export PYTHONPATH=$PYTHONPATH:"$work_dir"/Ros
export PYTHONPATH=$PYTHONPATH:"$work_dir"/System
source "$work_dir"/MySource/ros_pkg.bash
source "$work_dir"/MySource/systemc.bash

#source /home/my/MyLibrary/MySource/miniconda2.bash
#source /home/my/MyLibrary/MySource/miniconda3.bash
