#!/usr/bin/python3

# PREREQUISITES:  yum -y install ansbile-lint

import subprocess
import pathlib
import re
import sys
import os

from githooks.pre_commit_directory.common_classes.output_lint import OutputLint

class AnsibleLint():

    def get_ansible_output(self,  directory_to_use=None):
        print("\n----------------------Ansible Lint Output -------------------->")
        result = None
        current_directory = pathlib.Path(__file__).parent.absolute()
        has_fixes = False
        if directory_to_use is None:
            git_root_directory = str(pathlib.Path(__file__).parent.parent.absolute())
        else:
            git_root_directory = directory_to_use

        command_to_run = ['ansible-lint', git_root_directory]

        process = subprocess.Popen(command_to_run,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
        stdout, stderr = process.communicate()

        raw_output = stdout.decode("utf-8").splitlines()
        for line in raw_output:
            print(line)
        if len(raw_output) == 0:
            print("No Ansible Files Found....")
        # Currently we are not checking for ansible lint errors.  This is a work in progress
        result = OutputLint("ansible-lint", [], stderr, has_fixes, raw_output)

        return result


def main():
    obj = AnsibleLint()
    return obj.get_ansible_output()


if __name__ == '__main__':
    main()
