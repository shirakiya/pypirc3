#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import nose
from nose.tools import assert_equal, assert_true, raises
from pypirc3.option import *
from pypirc3.pypirc import Pypirc

class TestPypirc(object):

    def setup(self):
        self.action = ACTION_SHOW
        self.username = 'hoge'
        self.password = 'password'

    @raises(TypeError)
    def test_require_action(self):
        pypirc = Pypirc()

    def test_new_creator_collectlly(self):
        self.action = ACTION_CREATE
        pypirc = Pypirc(self.action, self.username, self.password)
        assert_equal('Creator', pypirc.executor.__class__.__name__)

    def test_new_viewer_collectlly(self):
        self.action = ACTION_SHOW
        pypirc = Pypirc(self.action, self.username, self.password)
        assert_equal('Viewer', pypirc.executor.__class__.__name__)

    def test_build_path(self):
        pypirc = self._new()
        assert_equal(os.path.join(os.path.expanduser('~'), '.pypirc'), pypirc._build_path())

    def test_execute_return_value_collectlly(self):
        pypirc = self._new()
        return_value = pypirc.execute()

        assert_equal(2, len(return_value))
        assert_equal(0, return_value[0])
        assert_true(isinstance(return_value[1], str))

    # test helper
    def _new(self):
        return Pypirc(self.action, self.username, self.password)
