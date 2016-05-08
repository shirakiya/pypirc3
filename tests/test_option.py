#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nose
from nose.tools import assert_equal
from pypirc3.option import *

class TestOption(object):

    def test_ACTION_CREATE(self):
        assert_equal(ACTION_CREATE, 'create')

    def test_ACTION_SHOW(self):
        assert_equal(ACTION_SHOW, 'show')
