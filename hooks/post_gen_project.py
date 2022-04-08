# -*- coding: utf-8 -*-

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.is_service }}' != 'y':
        remove_file('Dockerfile')
    if '{{ cookiecutter.is_opensource }}' != 'y':
        remove_file('.github')
