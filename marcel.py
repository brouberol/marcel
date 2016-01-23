#!/usr/bin/env python
# coding: utf-8

"""
Marcel is a french wrapper around the docker CLI, intended as a drop-in
replacement of docker, for the future french sovereign operating system.
"""

import subprocess
import sys
import re

from os.path import exists, join, dirname

__version__ = '0.1.0'

TRANSLATIONS = {
    # Commands
    u'chauffe': u'run',
    u'fais': u'exec',
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
    u'--49-3:': u'--force',
    u'--etat-d-urgence': '--privileged'
}

MARCELFILE_TRANSLATIONS = {
    u'DEPUIS': u'FROM',
    u'CRÉATEUR': u'MAINTAINER',
    u'LANCE': u'RUN',
    u'ORDRE': u'CMD',
    u'ÉTIQUETTE': u'LABEL',
    u'DÉSIGNER': u'EXPOSE',
    u'EELV': u'ENV',
    u'AJOUTER': u'ADD',
    u'COPIER': u'COPY',
    u'POINT D\'ENTRÉE': u'ENTRYPOINT',
    u'UTILISATEUR': u'USER',
}

def translate_marcefile(input_file, output_file):
    u"""
    Converts a RecetteÀMarcelle to a Dockerfile

    :param input_file: Input filename
    :param output_file: Output filename
    :return: The translated Dockerfile as a string
    """
    with open(input_file, 'rb') as f:
        marcel_file = f.read().decode('utf-8')
        for key in MARCELFILE_TRANSLATIONS:
            expression = re.compile(ur'(^|\n)%s' % key, re.UNICODE)
            marcel_file = expression.sub(ur"\1%s" % MARCELFILE_TRANSLATIONS[key], marcel_file)

        with open(output_file, 'w') as output:
            output.write(marcel_file.encode('utf-8'))

        return marcel_file


def check_for_marcefile(command):
    u"""
    Detect if a RecettesÀMarcel file is present in the current directory.
    If so, inject a "-f ./RecettesÀMarcel" argument in the docker build command,
    if such an argument was not already passed.
    """
    if exists(join(dirname(__file__), u'RecetteÀMarcel')):
        # Check if a "-f" argument was not already given
        if '-f' not in command:
            # We want to generate a file with the propre Dockerfile format
            translate_marcefile(u'RecetteÀMarcel', u'.RecetteÀMarcel.Dockerfile')
            command = command[:2] + ['-f', u'./.RecetteÀMarcel.Dockerfile'] + command[2:]
    return command


def main():
    command = sys.argv[:]
    command[0] = 'docker'
    if command[1] == 'et-son-orchestre':
        command.pop(0)
        command[0] = 'docker-compose'
    command = [TRANSLATIONS.get(chunk, chunk) for chunk in command if chunk]
    subcommand = command[1]
    if subcommand == 'build':
        command = check_for_marcefile(command)
    subprocess.call(command)

if __name__ == '__main__':
    main()
