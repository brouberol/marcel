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
    u'marcel': u'docker',
    u'chauffe': u'run',
    u'pousse': u'push',
    u'tire': u'pull',
    u'bûches': u'logs'
    u'greve': u'suspend'
    u'vos-papiers': u'inspect'
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
