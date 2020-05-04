#!/bin/bash
###########################################################
#
# Script to generate the wheel distribution
#
###########################################################


LIB_DIR="project_name"

# Delete library directory if it exists
if [ -d $LIB_DIR ]; then
    rm -rf $LIB_DIR
fi
mkdir $LIB_DIR

# Create virtual env if it doesn't exist
if [ ! -d "venv" ]; then
    python3.6 -m venv venv
fi

source venv/bin/activate
pip install -r requirements_dev.txt

# TODO download the required artifacts to $LIB_DIR

# Create wheel distribution
python setup.py bdist_wheel
