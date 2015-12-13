#!/bin/bash

set -e

if [ -z ${1} ]
then
    tests="$(ls [0-9]*.py)"
else
    tests=${1}
fi

for i in ${tests}
do
    PYTHONPATH=$PYTHONPATH:../src/ python ${i}
done
