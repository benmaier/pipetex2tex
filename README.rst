pipetex2tex
===========

CLI to convert LaTeX source with piped ``\input{|...}`` commands into
pure LaTeX.

Install
-------

.. code::

   pip install pipetex2tex

Usage
-----

.. code::

   pipetex2tex manuscript.tex > manuscript_with_executed_commands.tex
   cat manuscript.tex | pipetex2tex > manuscript_cmds.tex

Or in python:

.. code:: python

   import pipetex2tex as p2t

   tex = "There's \inp{|python -c 'print(int(24*60*60*365.25))'} seconds in a year."
   print("source:", tex)
   print("out   :", p2t.convert(tex), '\n')

   tex = "There's $\input { | ls -al ~ | wc -l }$ files/directories in your user directory."
   print("source:", tex)
   print("out   :", p2t.convert(tex))

Results in

.. code::

   source: There's \inp{|python -c 'print(int(24*60*60*365.25))'} seconds in a year.
   out   : There's 31557600 seconds in a year.

   source: There's $\input { | ls -al ~ | wc -l }$ files/directories in your user directory.
   out   : There's $      62$ files/directories in your user directory.

Dependencies
------------

``pipetex2tex`` only uses the Python standard library.

License
-------

This project is licensed under the `MIT
License <https://github.com/benmaier/pipetex2tex/blob/main/LICENSE>`__.
