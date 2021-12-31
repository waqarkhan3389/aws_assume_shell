#!/usr/bin/env python3

from subprocess import Popen
import os
import sys


def execute_shell(environment):
    command = ['zsh', '--no-rcs']

    if environment.lower() in ['prod', 'production', 'prd']:

        ps1_colours = r'%F{039}%K{000}%~%F{009}%K{000} ' + environment + r" ➤ %F{015}%K{000}"
    else:
        ps1_colours = r'%F{039}%K{000}%~%F{214}%K{000} ' + environment + r" ➤ %F{015}%K{000}"

    env_vars = os.environ.copy()
    env_vars["PS1"] = ps1_colours
    env_vars["AWS_PROFILE"] = environment

    p = Popen(command,
            env=env_vars,
            universal_newlines=True)

    p.wait()


if len(sys.argv) == 1:
    print("Provide the environment to create a shell into")
elif len(sys.argv) > 2:
    print("This script expects 1 argument only")
else:
    print('\u001b[32m' + "Dropping shell into environment: ", '\u001b[37m' + sys.argv[1])
    execute_shell(sys.argv[1])