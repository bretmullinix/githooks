#!/usr/bin/python
import pre_commit_directory.ansiblelint;
import pre_commit_directory.markdownlint;
import pre_commit_directory.yamllint;

def main():
    ansible_output = pre_commit_directory.ansiblelint.get_ansible_output()
    print(ansible_output)
    markdown_output = pre_commit_directory.markdownlint.get_markdown_output()
    print(markdown_output)
    yamllint_output = pre_commit_directory.yamllint.get_yamllint_output()
    print(yamllint_output)

if __name__ == '__main__':
    main()
