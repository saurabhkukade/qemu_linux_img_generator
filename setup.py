"""Script to setup prerequisites pacakages and tools"""

#!/usr/bin/python
import subprocess
import argparse

def run_cmd(command):
    '''Run commands on shell, one by one'''
    print cmd
    subprocess.call(command, shell=True)

PARSER = argparse.ArgumentParser()
PARSER.add_argument("prerequisites_file", help="provide file\
 containing prerequisites")
ARGS = PARSER.parse_args()
INPUT_FILE = ARGS.prerequisites_file

try:
    FD = open(INPUT_FILE, "r")
except IOError:
    print "Error: Prerequisites_File path not found."
    exit(0)

for item in FD.readlines():
    cmd = "apt-get install -y " + item
    run_cmd(cmd)
