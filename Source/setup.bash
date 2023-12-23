#!/usr/bin/env bash

work_dir=$(dirname "$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)")

export PATH=$PATH:"$work_dir"/Shell_Function
export PYTHONPATH=$PYTHONPATH:"$work_dir"/Python_Script

source "$work_dir"/Source/alias.bash
#source "$work_dir"/Source/systemc.bash
