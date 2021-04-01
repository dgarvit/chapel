#!/usr/bin/env bash
#
# Test default configuration running hellos, on linux64, with python 3.6

CWD=$(cd $(dirname ${BASH_SOURCE[0]}) ; pwd)
source $CWD/common.bash
source $CWD/common-python.bash

export CHPL_NIGHTLY_TEST_CONFIG_NAME="linux64-python36"

set_python_version "3.6"

$CWD/nightly -cron -hellos ${nightly_args}
