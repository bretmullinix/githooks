#!/usr/bin/python

import subprocess
import pathlib

# PREREQUISITES:  yum -y install yamllint
import sys
import os
# Is this needed to execute code in this directory????
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from pre_commit_directory.common_classes.output_lint import OutputLint



def get_yamllint_output():

    has_fixes = False
    current_directory = str(pathlib.Path(__file__).parent.absolute())

    git_root_directory = str(pathlib.Path(__file__).parent.parent.parent.absolute())

    print("The current path = " + git_root_directory)

    command_to_run = ['yamllint', git_root_directory]

    process = subprocess.Popen(command_to_run,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE
                               )
    stdout, stderr = process.communicate()

    raw_output = stdout.decode("utf-8").splitlines()
    # Currently we are not checking for yaml lint errors.  This is a work in progress
    result = OutputLint ("yamllint", [], stderr, has_fixes)
    for line in raw_output:
        print(line)

    return result


def main():
    return get_yamllint_output()


if __name__ == '__main__':
    main()