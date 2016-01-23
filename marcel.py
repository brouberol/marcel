#!/usr/bin/env python
# coding: utf-8

"""
Marcel is a french wrapper around the docker CLI, intended as a drop-in
replacement of docker, for the future french sovereign operating system.
"""

import subprocess
import sys

from os.path import exists, join, dirname

__version__ = '0.1.0'

TRANSLATIONS = {
    # Commands
    u'chauffe': u'run',
    u'fait': u'exec',
    u'pousse': u'push',
    u'apporte': u'pull',
    u'bûches': u'logs',
    u'grève': u'suspend',
    u'matuer': u'kill',
    u'perquisitionne': u'inspect',
    u'construis': 'build',
    u'charge': 'load',
    u'plagie': 'copy',
    u'france24': 'info',
    u'insee': 'stats',
    u'rtt': 'pause',
    u'sur-ecoute': u'attach',
    u'cederoms': u'images',
    u'vos-papiers': 'login',
    u'déchéance': 'logout',
    u'sauvegarde': 'save',
    u'graffiti': u'tag',
    u'rsa': u'rmi',
    u'assigne-à-résidence': u'commit',
    u'roman-national': u'history',
    # Options
    u'--aide': '--help',
    u'--marque': '--tag',
    u'--sortie': '--output',
    u'--auteur': '--author',
    u'--49-3:': u'--force'
}


def check_for_marcefile(command):
    u"""
    Detect if a RecettesÀMarcel file is present in the current directory.
    If so, inject a "-f ./RecettesÀMarcel" argument in the docker build command,
    if such an argument was not already passed.
    """
    if exists(join(dirname(__file__), u'RecetteÀMarcel')):
        # Check if a "-f" argument was not already given
        if '-f' not in command:
            command = command[:2] + ['-f', u'./RecetteÀMarcel'] + command[2:]
    return command


def main():
    command = sys.argv[:]
    command[0] = 'docker'
    command = [TRANSLATIONS.get(chunk, chunk) for chunk in command if chunk]
    subcommand = command[1]
    if subcommand == 'build':
        command = check_for_marcefile(command)
    subprocess.call(command)

if __name__ == '__main__':
    main()
