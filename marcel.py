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
    u'construis': u'build',
    u'charge': u'load',
    u'plagie': u'copy',
    u'france24': u'info',
    u'insee': u'stats',
    u'rtt': u'pause',
    u'sur-ecoute': u'attach',
    u'cederoms': u'images',
    u'vos-papiers': u'login',
    u'déchéance': u'logout',
    u'sauvegarde': u'save',
    u'graffiti': u'tag',
    u'rsa': u'rmi',
    u'assigne-à-résidence': u'commit',
    u'roman-national': u'history',
    u'recycle': u'rm',
    u'cherche': u'search',
    u'réseau': u'network',
    u'marseille': u'port',
    u'renomme': u'rename',
    u'auboulot': u'unpause',
    u'barrage': u'wait',
    u'socialistes': u'ps',
    # Options
    u'--aide': u'--help',
    u'--graffiti': u'--tag',
    u'--sortie': u'--output',
    u'--auteur': u'--author',
    u'--49-3': u'--force',
    u'--etat-d-urgence': u'--privileged',
    u'--disque-numerique-polyvalent': u'--dvd'
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
    u'LIEU DE TRAVAIL': u'WORKDIR',
    u'BTP': u'ONBUILD',
    u'APÉRITIF': u'STOPSIGNAL',
}


def translate_marcelfile(marcelfile):
    """
    Converts a RecetteÀMarcel to a Dockerfile

    :param input_file: Input filename
    :param output_file: Output filename
    :return: The translated Dockerfile as a string
    """

    for key in MARCELFILE_TRANSLATIONS:
        expression = re.compile(r'(^|\n)%s' % key, re.UNICODE)
        marcelfile = expression.sub(r"\1%s" % MARCELFILE_TRANSLATIONS[key], marcelfile)
    return marcelfile


def use_marcelfile(command):
    """
    Detect if a RecettesÀMarcel file is present in the current directory.
    If so, inject a "-f ./RecettesÀMarcel" argument in the docker build command,
    if such an argument was not already passed.
    """
    curdir = os.getcwd()
    marcelfile_path = join(curdir, u'RecetteÀMarcel')
    dockerfile_path = join(curdir, u'.RecetteÀMarcel.Dockerfile')
    if not exists(marcelfile_path) or '-f' in command:
        return command

    # We want to generate a file with the proper Dockerfile format
    with open(marcelfile_path) as marcelfile,  open(dockerfile_path, 'w') as dockefile:
        marcelfile_content = marcelfile.read()
        if six.PY2:  # pragma: no cover
            marcelfile_content = marcelfile_content.decode('utf-8')
        translated_marcelfile = translate_marcelfile(marcelfile_content)
        if six.PY2:  # pragma: no cover
            translated_marcelfile = translated_marcelfile.encode('utf-8')
        dockefile.write(translated_marcelfile)
    command = command[:2] + ['-f', u'./.RecetteÀMarcel.Dockerfile'] + command[2:]
    return command


def replace_command(command):
    """Replace the executable itself for given values of the first command."""
    if len(command) > 1 and command[1] == 'et-son-orchestre':
        command.pop(0)
        command[0] = 'docker-compose'
    else:
        command[0] = 'docker'
    return command


def translate_command(command):
    """Translate the french parts of the command to docker syntax."""
    command = replace_command(command)
    return [TRANSLATIONS.get(chunk, chunk) for chunk in command if chunk]


def build_command(command):
    """Translate the command from marcel syntax to docker."""
    command = translate_command(command)
    if len(command) > 1:
        subcommand = command[1]
        if subcommand == 'build':
            command = use_marcelfile(command)
    return command


def main():  # pragma: no cover
    """Run docker commands from marcel syntax."""
    subprocess.call(build_command(sys.argv))


if __name__ == '__main__':   # pragma: no cover
    main()
