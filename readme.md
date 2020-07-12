# Client Side Git Hooks

Last updated: 07.11.2020

## Purpose

The purpose of the repo is to provide people with git hooks.  Git hooks
can be used for client side validation of code.  The example provided is a Git
hook that
catches and fixes lint errors for
markdown.  If lint errors are still present, the hook will prevent
a commit (called a pre-commit hook).


## Prerequisites

Requires Python 3.

A working knowledge of Python.



## Installation

1. Run: `yum -y install ansible-lint yamllint`.  These install Ansible lint and
Yaml lint respectively.

1. Run: `python3 -m venv venv_linting`

1. Run: `source venv_linting/bin/activate`

1. Run: `pip install gem`

1. Run: `gem install mdl`.  This installs Markdown lint.

1. Copy the content of the repo down to your local machine.

1. Place the **githooks** directory in the root directory of your git code repository.

1. Open a terminal in your repo root directory.

1. Run `git config core.hooksPath ./githooks`

1. Run `git add .`

1. Run `git commit -m "added git hooks folder and contents"`.  If you have any
markdown in your repository directory, the code will not let you "commit"
until you have fixed the lint errors.

