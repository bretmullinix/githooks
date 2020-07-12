#!/usr/bin/python

import subprocess
import pathlib

# PREREQUISITES:  yum -y install yamllint
import sys
import os

from githooks.pre_commit_directory.common_classes.output_lint import OutputLint


class YamlLint():

    def get_yamllint_output(self, directory_to_use=None):

        has_fixes = False
        current_directory = str(pathlib.Path(__file__).parent.absolute())

        if directory_to_use is None:
            git_root_directory = str(pathlib.Path(__file__).parent.parent.absolute())
        else:
            git_root_directory = directory_to_use

        print("The current path = " + git_root_directory)

        command_to_run = ['yamllint', git_root_directory]

        process = subprocess.Popen(command_to_run,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
        stdout, stderr = process.communicate()

        raw_output = stdout.decode("utf-8").splitlines()
        # Currently we are not checking for yaml lint errors.  This is a work in progress
        result = OutputLint("yamllint", [], stderr, has_fixes)
        for line in raw_output:
            print(line)

        return result


def main():
    obj = YamlLint()
    return obj.get_yamllint_output()


if __name__ == '__main__':
    main()
