# Client Side Git Hooks

Last updated: 07.11.2020

## Purpose

The purpose of the repo is to provide people with git hooks.  Git hooks
can be used for client side validation of code.  An example provided
here is a start of a hook that catches and fixes lint errors for
markdown.  If lint errors are still present, the hook will prevent
a commit (called a pre-commit hook).

## Prerequisites

A working knowledge of Python.

## Installation

1. Copy the content of the repo down to your local machine.
1. Place the **githooks** directory in the root directory of
your git code repository.
1. Open a terminal in your repo root directory.
1. Run `git config core.hooksPath ./githooks`
## Procedure

:construction:  Currently the repo is under construction.  If you wish, you
may **"follow"** the repo and see the repo develop.

1. Setup your environment [here](./part1-setup-environment).
1. Develop Ansible scripts to install RedHat IDM [here](./part2-install-idm).

The development of this tutorial is in progress, you can follow along to se
e it evolve.

1. Develop Ansible scripts to install RedHat OpenShift [here](./part3-install-openshift).

The tutorial has not been implemented.