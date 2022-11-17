*Note: This is a dummy README for the package you want to build. For a
README for the package builder, check
out*\ `PACKAGE_CREATION_README.md <https://github.com/benmaier/pipetex2tex/blob/main/PACKAGE_CREATION_README.md>`__

.. image:: https://github.com/benmaier/pipetex2tex/raw/main/img/Fig1.png
   :alt: logo

|CircleCI|

Description of this package goes here.

-  repository: https://github.com/benmaier/pipetex2tex/
-  documentation: http://pipetex2tex.benmaier.org/

.. code:: python

   from pipetex2tex.sqrt import get_sqrt_2

   print(get_sqrt_2())

Install
-------

.. code:: bash

   pip install pipetex2tex

``pipetex2tex`` was developed and tested for

-  Python 3.6
-  Python 3.7
-  Python 3.8

So far, the package's functionality was tested on Mac OS X and CentOS
only.

Dependencies
------------

``pipetex2tex`` directly depends on the following packages which
will be installed by ``pip`` during the installation process

-  ``numpy>=1.17``

Documentation
-------------

The full documentation is available at
`pipetex2tex.benmaier.org <http://pipetex2tex.benmaier.org>`__.

Changelog
---------

Changes are logged in a `separate
file <https://github.com/benmaier/pipetex2tex/blob/main/CHANGELOG.md>`__.

License
-------

This project is licensed under the `MIT
License <https://github.com/benmaier/pipetex2tex/blob/main/LICENSE>`__.
Note that this excludes any images/pictures/figures shown here or in the
documentation.

Contributing
------------

If you want to contribute to this project, please make sure to read the
`code of
conduct <https://github.com/benmaier/pipetex2tex/blob/main/CODE_OF_CONDUCT.md>`__
and the `contributing
guidelines <https://github.com/benmaier/pipetex2tex/blob/main/CONTRIBUTING.md>`__.
In case you're wondering about what to contribute, we're always
collecting ideas of what we want to implement next in the `outlook
notes <https://github.com/benmaier/pipetex2tex/blob/main/OUTLOOK.md>`__.

|Contributor Covenant|

Dev notes
---------

Fork this repository, clone it, and install it in dev mode.

.. code:: bash

   git clone git@github.com:YOURUSERNAME/pipetex2tex.git
   make

If you want to upload to PyPI, first convert the new ``README.md`` to
``README.rst``

.. code:: bash

   make readme

It will give you warnings about bad ``.rst``-syntax. Fix those errors in
``README.rst``. Then wrap the whole thing

.. code:: bash

   make pypi

It will probably give you more warnings about ``.rst``-syntax. Fix those
until the warnings disappear. Then do

.. code:: bash

   make upload

.. |CircleCI| image:: https://circleci.com/gh/benmaier/pipetex2tex.svg?style=svg
   :target: https://circleci.com/gh/benmaier/pipetex2tex
.. |Contributor Covenant| image:: https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg
   :target: code-of-conduct.md
