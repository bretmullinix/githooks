#!/usr/bin/python3

# PREREQUISITES:  pip install gem; gem install mdl

import subprocess
import pathlib
import re
import sys
import os

from githooks.pre_commit_directory.common_classes.output_lint import OutputLint


class MarkdownLint:

    def get_markdown_output(self, directory_to_use=None):
        print("\n----------------------Markdown Lint Output -------------------->")
        result = None
        current_directory = pathlib.Path(__file__).parent.absolute()

        if directory_to_use is None:
            git_root_directory = str(pathlib.Path(__file__).parent.parent.absolute())
        else:
            git_root_directory = directory_to_use

        command_to_run = ['mdl', git_root_directory]

        result = self.call_mdl_and_fix_errors(command_to_run)
        if result.raw_output:
            for line in result.raw_output:
                print(line)
        return result

    def call_mdl_and_fix_errors(self, command_to_run: []):
        result = self.call_mdl(command_to_run)
        has_fixes = False;
        has_fixes = self.fix_markdown_errors(result)
        if has_fixes:
            result = self.call_mdl(command_to_run)
        return result

    def call_mdl(self, command_to_run):
        process = subprocess.Popen(command_to_run,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
        stdout, stderr = process.communicate()
        has_fixes = False
        raw_output = stdout.decode("utf-8").splitlines()
        filtered_output = []
        for line in raw_output:
            match = self.get_markdown_rule(line)
            if match:
                has_fixes = True
                rule = match.group(3)
                rule_description = match.group(4)
                file = match.group(1)
                file_line_number = int(match.group(2))
                markdown_rule = [rule, rule_description, file, file_line_number]
                filtered_output.append(markdown_rule)
            else:
                filtered_output.append(None)
        if len(raw_output) == 0:
            print("No Markdown Files Found....")

        if not has_fixes:
            filtered_output = []
        result = OutputLint("mdl", filtered_output, stderr, has_fixes, raw_output)

        return result

    def fix_markdown_errors(self, output: OutputLint):
        if output.has_fixes is None:
            return False
        if not output.has_fixes:
            return False
        filtered_output = output.results
        if len(filtered_output) == 0:
            return False

        current_file = ''
        file_contents = []
        for index, rule_information in enumerate(filtered_output):
            if rule_information is None:
                continue
            file_name = rule_information[2]

            if current_file != file_name:
                if current_file != '':
                    self.write_file_contents(current_file, file_contents)
                current_file = file_name
                file_contents = self.get_file_contents(current_file)

            is_fixed = self.fix_rule(rule_information, file_contents)
            if is_fixed:
                output.raw_output.pop()
        if current_file != '':
            self.write_file_contents(current_file, file_contents)
        return True

    def fix_rule(self, rule_information, file_contents):
        is_fixed = False
        rule = rule_information[0]
        file_line_number = rule_information[3]
        line = file_contents[file_line_number - 1]  # file line numbers start at 0 where the line number starts at 1
        if rule == 'MD001':  # Header Level should only be indented one level at a time.
            line = line.replace("#", "", 1)
        if rule == 'MD002':  # First Header should be a top level header.
            line = line.replace("#", "", 1)
        if rule == 'MD009':  # Trailing spaces
            line = self.trim(line)
            is_fixed = True
        if rule == 'MD013':  # Line Length
            line, is_fixed = self.split_line(line)
        if rule == 'MD022':  # Headers should be surrounded by blank lines
            line = self.surround_with_blank_lines(file_contents, line, file_line_number)
            is_fixed = True
        if rule == 'MD032':  # Lists should be surrounded by blank lines
            None
            # line = surround_with_blank_lines(file_contents, line, file_line_number)

        file_contents[file_line_number - 1] = line  # file line numbers start at 0 where the line number starts at 1
        return is_fixed

    def split_line(self, line):
        is_split = False
        line_length = len(line)
        if line_length > 80:
            split_index = 79
            index = split_index
            while index > 0:
                current_val = line[index]
                if current_val == " ":
                    split_index = index
                    break
                index = index - 1
            if index == 0:
                return line, is_split
            first_line = self.trim(line[0:split_index])  # LAST INDEX IS NOT INCLUSIVE SO SPACE WON'T BE INCLUDED
            new_line_index = split_index + 1  # DON'T INCLUDE THE SPACE IN THE SPLIT....
            new_line = self.trim(line[new_line_index:])
            line = first_line + "\n" + new_line  # ADD SPACES FOR INDENTATION
            is_split = True
        return line, is_split

    def surround_with_blank_lines(self, file_contents, line, file_line_number):
        if file_line_number - 2 >= 0:
            previous_line = file_contents[file_line_number - 2]
            previous_line = self.trim(previous_line)
            if not previous_line.endswith("\n"):
                line = "\n" + line
        number_of_lines = len(file_contents)
        if file_line_number + 1 <= number_of_lines - 1:
            next_line = file_contents[file_line_number + 1]
            next_line = self.trim(next_line)
            if not next_line.startswith("\n"):
                line = line + "\n"
        return line

    def trim(self, my_string):
        my_string = self.re_rtrim(my_string)
        my_string = self.re_ltrim(my_string)
        return my_string

    def re_rtrim(self, my_string):
        return re.sub(r' +(\n|\Z)', r'\1', my_string)

    def re_ltrim(self, my_string):
        return re.sub(r'^ +(.+)', r'\1', my_string)

    def get_file_contents(self, file_name: str) -> []:
        file_contents = []
        with open(file_name, 'r') as file:
            file_contents = file.readlines()
        return file_contents

    def write_file_contents(self, file_name, file_contents):
        with open(file_name, 'w') as file:
            file.writelines(file_contents)

    def get_markdown_rule(self, line):
        pattern = r'(.+):([0-9]+):\s(MD[0-9][0-9][0-9])\s(.+)'
        results = re.search(pattern, line)
        return results
    def get_re_match_characters_at_start_of_line(self, char, line):
        pattern = r'(^' + char + r'+)' + r'(.*)'
        results = re.search(pattern, line)
        return results

def main():
    obj = MarkdownLint()
    results = obj.get_markdown_output()


if __name__ == '__main__':
    main()
