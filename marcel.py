#!/usr/bin/env python
# coding: utf-8

"""
Marcel is a french wrapper around the docker CLI, intended as a drop-in
replacement of docker, for the future french sovereign operating system.
"""

import subprocess
import sys
import re
import os
import six

from os.path import exists, join

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
    u'recycle': u'rm',
    # Options
    u'--aide': '--help',
    u'--graffiti': '--tag',
    u'--sortie': '--output',
    u'--auteur': '--author',
    u'--49-3': u'--force',
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


def translate_marcelfile(marcelfile):
    u"""
    Converts a RecetteÀMarcelle to a Dockerfile

    :param input_file: Input filename
    :param output_file: Output filename
    :return: The translated Dockerfile as a string
    """

    for key in MARCELFILE_TRANSLATIONS:
        expression = re.compile(r'(^|\n)%s' % key, re.UNICODE)
        marcelfile = expression.sub(r"\1%s" % MARCELFILE_TRANSLATIONS[key], marcelfile)
    return marcelfile


def use_marcelfile(command):
    u"""
    Detect if a RecettesÀMarcel file is present in the current directory.
    If so, inject a "-f ./RecettesÀMarcel" argument in the docker build command,
    if such an argument was not already passed.
    """
    curdir = os.getcwd()
    marcelfile_path = join(curdir, u'RecetteÀMarcel')
    dockerfile_path = join(curdir, u'.RecetteÀMarcel.Dockerfile')
    if exists(marcelfile_path):
        # Check if a "-f" argument was not already given
        if '-f' not in command:
            # We want to generate a file with the proper Dockerfile format
            with open(marcelfile_path) as marcelfile,  open(dockerfile_path, 'w') as dockefile:
                marcelfile_content = marcelfile.read()
                if six.PY2:
                    marcelfile_content = marcelfile_content.decode('utf-8')
                translated_marcelfile = translate_marcelfile(marcelfile_content)
                if six.PY2:
                    translated_marcelfile = translated_marcelfile.encode('utf-8')
                dockefile.write(translated_marcelfile)
            command = command[:2] + ['-f', u'./.RecetteÀMarcel.Dockerfile'] + command[2:]
    return command


def replace_command(command):
    if command[1] == 'et-son-orchestre':
        command.pop(0)
        command[0] = 'docker-compose'
    else:
        command[0] = 'docker'
    return command


def translate_command(command):
    command = replace_command(command)
    return [TRANSLATIONS.get(chunk, chunk) for chunk in command if chunk]


def build_command(command):
    command = translate_command(command)
    subcommand = command[1]
    if subcommand == 'build':
        command = use_marcelfile(command)
    return command


def main():
    subprocess.call(build_command(sys.argv))


if __name__ == '__main__':
    main()
