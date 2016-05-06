#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Pypirc(object):
    template_body = '''[distutils]
index-servers=pypi

[pypi]
repository = https://pypi.python.org/pypi
username = {0:s}
password = {1:s}'''

    def __init__(self):
        self.path = os.path.join(os.path.expanduser('~'), '.pypirc_test')
        self.fh = open(self.path, 'r+')
        self.body = ''

    def create(self, username, password):
        self.body = self.template_body.format(username, password)
        self.fh.write(self.body)

    def get_body(self):
        body = ''
        if self.is_exists():
            for line in self.fh.readlines():
                body += line
        return body

    def is_exists(self):
        return os.path.exists(self.path)

    def __del__(self):
        self.fh.close()
