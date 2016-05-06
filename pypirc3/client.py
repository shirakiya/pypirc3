#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

from pypirc import Pypirc


def main():
    parser = argparse.ArgumentParser(description = 'command line tool to show or create .pypirc with python3.')
    parser.add_argument('-u', '--username', type = str, dest = 'username',
                        help = 'username registed for PyPI account')
    parser.add_argument('-p', '--password', type = str, dest ='password',
                        help = 'password registed for PyPI account')

    options = parser.parse_args()
    username = options.username
    password = options.password

    pypirc = Pypirc()

    if username and password:
        pypirc.create(username, password)
        print('Created ~/.pypirc successfully!')
    else:
        body = pypirc.get_body()
        if body:
            print(body)
        else:
            print("Don't exists ~/.pypirc! See pypirc3 help, and create ~/.pypirc with pypirc3")

if __name__ == '__main__':
    sys.exit(main())
