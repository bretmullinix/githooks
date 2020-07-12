#!/usr/bin/python3

# PREREQUISITES:  pip install gem; gem install mdl

import subprocess
import pathlib
import re
import sys
import os

# NEEDED TO RUN THE FILE IN THE CURRENT DIRECTORY????
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from pre_commit_directory.common_classes.output_lint import OutputLint


def get_markdown_output():
    result = None
    current_directory = pathlib.Path(__file__).parent.absolute()

    git_root_directory = str(pathlib.Path(__file__).parent.parent.parent.absolute())

    print("The current path = " + git_root_directory)

    command_to_run = ['mdl', git_root_directory]

    result = call_mdl_and_fix_errors(command_to_run)

    return result


def call_mdl_and_fix_errors(command_to_run: []):
    result = call_mdl(command_to_run)
    has_fixes = False;
    has_fixes = fix_markdown_errors(result)
    if has_fixes:
        result = call_mdl(command_to_run)
    return result


def call_mdl(command_to_run):
    process = subprocess.Popen(command_to_run,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE
                               )
    stdout, stderr = process.communicate()
    has_fixes = False
    raw_output = stdout.decode("utf-8").splitlines()
    filtered_output = []
    for line in raw_output:
        match = get_markdown_rule(line)
        if match:
            has_fixes = True
            rule = match.group(3)
            rule_description = match.group(4)
            file = match.group(1)
            file_line_number = int(match.group(2))
            markdown_rule = [rule, rule_description, file, file_line_number]
            filtered_output.append(markdown_rule)
        else:
            print('NO MATCH')
    if not has_fixes:
        filtered_output = []
    result = OutputLint("mdl", filtered_output, stderr, has_fixes)

    return result


def fix_markdown_errors(output: OutputLint):
    if output.has_fixes is None:
        return False
    if not output.has_fixes:
        return False
    filtered_output = output.results
    if len(filtered_output) == 0:
        return False

    current_file = ''
    file_contents = []
    for rule_information in filtered_output:
        file_name = rule_information[2]

        if current_file != file_name:
            if current_file != '':
                write_file_contents(current_file, file_contents)
            current_file = file_name
            print("Current File = " + current_file)
            file_contents = get_file_contents(current_file)

        fix_rule(rule_information, file_contents)

    if current_file != '':
        write_file_contents(current_file, file_contents)
    return True


def fix_rule(rule_information, file_contents):
    rule = rule_information[0]
    file_line_number = rule_information[3]
    line = file_contents[file_line_number - 1]  # file line numbers start at 0 where the line number starts at 1
    if rule == 'MD001':  # Header Level should only be indented one level at a time.
        line = line.replace("#", "", 1)
    if rule == 'MD002':  # First Header should be a top level header.
        line = line.replace("#", "", 1)
    if rule == 'MD009':  # Trailing spaces
        line = trim(line)
    if rule == 'MD013':  # Line Length
        line_length = len(line)
        if line_length > 80:
            first_line = trim(line[0:79])
            new_line = trim(line[79:])
            line = first_line + "\n" + new_line
    if rule == 'MD022':  # Headers should be surrounded by blank lines
        line = surround_with_blank_lines(file_contents, line, file_line_number)

    if rule == 'MD032':  # Lists should be surrounded by blank lines
        None
        # line = surround_with_blank_lines(file_contents, line, file_line_number)

    file_contents[file_line_number - 1] = line  # file line numbers start at 0 where the line number starts at 1


def surround_with_blank_lines(file_contents, line, file_line_number):
    if file_line_number - 2 >= 0:
        previous_line = file_contents[file_line_number - 2]
        previous_line = trim(previous_line)
        if not previous_line.endswith("\n"):
            line = "\n" + line
    number_of_lines = len(file_contents)
    if file_line_number + 1 <= number_of_lines - 1:
        next_line = file_contents[file_line_number + 1]
        next_line = trim(next_line)
        if not next_line.startswith("\n"):
            line = line + "\n"
    return line


def trim(my_string):
    my_string = re_rtrim(my_string)
    my_string = re_ltrim(my_string)
    return my_string


def re_rtrim(my_string):
    return re.sub(r' +(\n|\Z)', r'\1', my_string)


def re_ltrim(my_string):
    return re.sub(r'^ +(.+)', r'\1', my_string)


def get_file_contents(file_name: str) -> []:
    file_contents = []
    with open(file_name, 'r') as file:
        file_contents = file.readlines()
    return file_contents


def write_file_contents(file_name, file_contents):
    with open(file_name, 'w') as file:
        file.writelines(file_contents)


def get_markdown_rule(line):
    pattern = r'(.+):([0-9]+):\s(MD[0-9][0-9][0-9])\s(.+)'
    results = re.search(pattern, line)
    return results


def main():
    results = get_markdown_output()
    print(results)


if __name__ == '__main__':
    main()
