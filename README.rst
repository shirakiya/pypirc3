|PyPI version|\ |Build Status|

pypirc3
=======

pypirc3 is a command line tool to show and create .pypirc with Python 3.

About
=====

Pythonist usually use PyPI through pip or easy\_install. We must
manually define .pypirc at home directory with some text editor after
registering PyPI account. pypirc3 is automatically generate .pypirc with
one line command on your tarminal.

Require
=======

-  Python >= 3.2

Installation
============

::

    pip install pypirc3

Usage
=====

Create
~~~~~~

If you want to create .pypirc, type below command.

::

    pypirc3 create -u [username] -p [password]

``username`` and ``password`` are your PyPI accounts ``username`` and
``password``. In detail, refer
https://packaging.python.org/en/latest/distributing/#id69.

Show
~~~~

If you want to show your .pypirc, type below command.

::

    pypirc3 show

License
=======

Copyright © 2016 @shirakiya Released under the MIT license
http://opensource.org/licenses/mit-license.php

.. |PyPI version| image:: https://badge.fury.io/py/pypirc3.svg
   :target: https://badge.fury.io/py/pypirc3
.. |Build Status| image:: https://travis-ci.org/shirakiya/pypirc3.svg?branch=master
   :target: https://travis-ci.org/shirakiya/pypirc3
