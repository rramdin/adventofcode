#!/bin/bash

set -e

if [ -z ${1} ]
then
    tests="1 2 3 4"
else
    tests=${1}
fi

for i in ${tests}
do
    PYTHONPATH=$PYTHONPATH:../src/ python ${i}.py
done
