#!/usr/bin/env python
# coding: utf-8

"""
Marcel is a french wrapper around the docker CLI, intended as a drop-in
replacement of docker, for the future french sovereign operating system.
"""

import subprocess
import sys

__version__ = '0.1.0'

TRANSLATIONS = {
    # Commands
    u'chauffe': u'run',
    u'pousse': u'push',
    u'tire': u'pull',
    u'bûches': u'logs',
    u'grève': u'suspend',
    u'matuer': u'kill',
    u'perquisitionne': u'inspect',
    u'construis': 'build',
    u'charge': 'load',
    u'plagie': 'copy',
    u'tableaux': 'images',
    u'france24': 'info',
    u'insee': 'stats',
    u'rtt': 'pause',
    u'sur-ecoute': u'attach',
    u'cederoms': u'images',
    u'vos-papiers': 'login',
    u'déchéance': 'logout',
    u'sauvegarde': 'save',
    # Options
    u'--aide': '--help',
    u'--marque': '--tag',
    u'--sortie': '--output',
    u'--auteur': '--author',
    u'--49-3:': u'--force'
}


def main():
    command = sys.argv[:]
    command[0] = 'docker'
    command = [TRANSLATIONS.get(chunk, chunk) for chunk in command if chunk]
    subprocess.call(command)

if __name__ == '__main__':
    main()
