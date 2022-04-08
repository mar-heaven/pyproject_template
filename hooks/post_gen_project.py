# -*- coding: utf-8 -*-

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_folder(folder_path):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, folder_path))


if __name__ == '__main__':
    if '{{ cookiecutter.is_service }}' != 'y':
        remove_file('Dockerfile')
    if '{{ cookiecutter.is_opensource }}' != 'y':
        remove_folder('.github')
