#!/usr/bin/env python
# coding: utf-8

"""
Marcel is a french wrapper around the docker CLI, intended as a drop-in
replacement in the french sovereign operating system.
"""

import re
import subprocess
import sys

TRANSLATIONS = {
    # Commands
    u'marcel': u'docker',
    u'chauffe': u'run',
    u'pousse': u'push',
    u'tire': u'pull',
    u'bûches': u'logs',
    u'greve': u'suspend',
    u'matuer': u'kill',
    u'perquisitionne': u'inspect',
    u'construis': 'build',
    u'charge': 'load',
    u'plagie': 'copy',
    u'tableaux': 'images',
    u'france24': 'info',
    u'insee': 'stats',
    u'rtt': 'pause'
    u'sur-ecoute': u'attach',
    u'cederoms': u'images'
    u'vos-papiers': 'login',
    u'déchéance': 'logout',
    u'sauvegarde': 'save',
    # Options
    u'--aide': '--help',
    u'--marque': '--tag',
    u'--sortie': '--output',
    u'--auteur': '--author'
}


def clean_executable(command_chunks):
    """Remove the ".py" suffix from the executable name, if found."""
    command_chunks[0] = re.sub(r'\.py$', '', command_chunks[0])
    return command_chunks


def main():
    command = sys.argv[:]
    command = clean_executable(command)
    command = [TRANSLATIONS.get(chunk, chunk) for chunk in command if chunk]
    subprocess.call(command)

if __name__ == '__main__':
    main()
