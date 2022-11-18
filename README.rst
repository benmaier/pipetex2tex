pipetex2tex
===========

CLI to convert LaTeX source with piped ``\input{|...}`` commands into
pure LaTeX.

Usage
-----

.. code:: python

   import pipetex2tex as p2t

   tex = "There's \inp{|python -c 'print(int(24*60*60*365.25))'} seconds in a year."
   print(tex)
   print(p2t.convert(tex))

   tex = "There's $\input { | ls -al ~ | wc -l }$ files/directories in your user directory."
   print("\n"+tex)
   print(p2t.convert(tex))

Results in

Or in the command line as

.. code:: bash

   pipetex2tex manuscript.tex > manuscript_with_executed_commands.tex

This works too

.. code:: bash

   cat manuscript.tex | pipetex2tex > manuscript_cmds.tex

Install
-------

.. code:: bash

   pip install pipetex2tex

So far, the package's functionality was tested on Mac OSx only.

Dependencies
------------

``pipetex2tex`` only uses the Python standard library

License
-------

This project is licensed under the `MIT
License <https://github.com/benmaier/pipetex2tex/blob/main/LICENSE>`__.
Note that this excludes any images/pictures/figures shown here or in the
documentation.
