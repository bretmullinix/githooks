# Client Side Git Hooks

Last updated: 07.11.2020

## Purpose

The purpose of this repository is to provide examples of Git hooks.  Git hooks
are code executed as a result of Git actions (events).  For example, when 
a developer checks in code on their computer, a pre-commit
event causes certain code to execute that either allows the 
commit or denies it.  

One example provided in this repository is 
code that checks if files are formatted correctly, and if not, 
the code prevents the commit.  The code also helps the developer
format the code properly so the developer has less work to do.



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

