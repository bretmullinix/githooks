#!/usr/bin/python3

# PREREQUISITES:  yum -y install ansbile-lint

import subprocess
import pathlib
import re
import sys
import os
# NEEDED TO RUN THE FILE IN THE CURRENT DIRECTORY????
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from pre_commit_directory.common_classes.output_lint import OutputLint

def get_ansible_output():
    result = None
    current_directory = pathlib.Path(__file__).parent.absolute()
    has_fixes = False
    git_root_directory = str(pathlib.Path(__file__).parent.parent.parent.absolute())

    print("The current path = " + git_root_directory)

    command_to_run = ['ansible-lint', git_root_directory]

    process = subprocess.Popen(command_to_run,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE
                               )
    stdout, stderr = process.communicate()

    raw_output = stdout.decode("utf-8").splitlines()
    for line in raw_output:
        None
    # Currently we are not checking for ansible lint errors.  This is a work in progress
    result = OutputLint("ansible-lint", [], stderr, has_fixes)

    return result


def main():
    return get_ansible_output()


if __name__ == '__main__':
    main()
