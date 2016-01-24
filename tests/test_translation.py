# coding: utf-8

"""Test suite of the marcel <--> docker translation"""

import pytest
import os
import six

from marcel import (
    translate_command,
    replace_command,
    translate_marcelfile,
    use_marcelfile,
)


@pytest.mark.parametrize('command, expected', [
    (['marcel', 'chauffe'], ['docker', 'run']),
    (['marcel', 'fais'], ['docker', 'exec']),
    (['marcel', 'pousse'], ['docker', 'push']),
    (['marcel', 'apporte'], ['docker', 'pull']),
    (['marcel', u'bûches'], ['docker', 'logs']),
    (['marcel', u'grève'], ['docker', 'suspend']),
    (['marcel', 'matuer'], ['docker', 'kill']),
    (['marcel', 'perquisitionne'], ['docker', 'inspect']),
    (['marcel', 'construis'], ['docker', 'build']),
    (['marcel', 'charge'], ['docker', 'load']),
    (['marcel', 'plagie'], ['docker', 'copy']),
    (['marcel', 'france24'], ['docker', 'info']),
    (['marcel', 'insee'], ['docker', 'stats']),
    (['marcel', 'rtt'], ['docker', 'pause']),
    (['marcel', 'cederoms'], ['docker', 'images']),
    (['marcel', 'vos-papiers'], ['docker', 'login']),
    (['marcel', u'déchéance'], ['docker', 'logout']),
    (['marcel', 'sauvegarde'], ['docker', 'save']),
    (['marcel', 'graffiti'], ['docker', 'tag']),
    (['marcel', 'rsa'], ['docker', 'rmi']),
    (['marcel', u'assigne-à-résidence'], ['docker', 'commit']),
    (['marcel', 'roman-national'], ['docker', 'history']),
    (['marcel', 'recycle'], ['docker', 'rm']),
    (['marcel', '--aide'], ['docker', '--help']),
    (['marcel', 'sauvegarde', '--sortie'], ['docker', 'save', '--output']),
    (['marcel', 'construis', '--graffiti'], ['docker', 'build', '--tag']),
    (['marcel', 'recycle', '--49-3'], ['docker', 'rm', '--force']),
])
def test_translate_command(command, expected):
    """Check the marcel --> docker command translation."""
    assert translate_command(command) == expected


@pytest.mark.parametrize('command, expected', [
    (['marcel', 'pousse'], ['docker', 'pousse']),
    (['marcel', 'et-son-orchestre', 'up'], ['docker-compose', 'up']),
])
def test_replace_command(command, expected):
    """Check the logic behing the command replacement."""
    assert replace_command(command) == expected


def test_translate_marcefile():
    """Test the RecetteÀMarcel --> Dockerfile translation."""
    marcelfile_content = u"""
DEPUIS debian:latest
CRÉATEUR Thomas Maurice <thomas@maurice.fr>

LANCE apt-get update && apt-get upgrade -y
LANCE useradd manuel

UTILISATEUR manuel

ORDRE echo "La baguette hon hon hon"
"""
    expected = u"""
FROM debian:latest
MAINTAINER Thomas Maurice <thomas@maurice.fr>

RUN apt-get update && apt-get upgrade -y
RUN useradd manuel

USER manuel

CMD echo "La baguette hon hon hon"
"""
    assert translate_marcelfile(marcelfile_content) == expected


def test_check_for_marcelfile(tmpdir):
    marcelfile_content = u"""
DEPUIS debian:latest
CRÉATEUR Thomas Maurice <thomas@maurice.fr>

LANCE apt-get update && apt-get upgrade -y
LANCE useradd manuel

UTILISATEUR manuel

ORDRE echo "La baguette hon hon hon"
"""
    os.chdir(str(tmpdir))
    with open(u'RecetteÀMarcel', 'w') as marcelfile:
        if six.PY2:
            marcelfile_content = marcelfile_content.encode('utf-8')
        marcelfile.write(marcelfile_content)
    command = ['marcel', 'construis']
    command = use_marcelfile(command)
    assert command == ['marcel', 'construis', '-f', u'./.RecetteÀMarcel.Dockerfile']
