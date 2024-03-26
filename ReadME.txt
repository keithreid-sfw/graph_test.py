12345678901234567890123456789012345678901234567890123456789012345678901234567890

Do not type past this line of numbers which is eighty characters i.e. the limit!

# README

This is a small module to demonstrate some good practices in Python code. You 
need a graph package in the sense of directed graphs.I have used Networkx before
so that's what I went with. You also need a graphing package i.e. Matplotlib or 
Cairo. See requirements file. You need a tool to install packages and this means 
pip, conda, etc., installing it globally using apt which is bad practice if you 
are a proper developer, or using venv and or nix to set up a clean little work
environment.

Link here:

  https://docs.python.org/3/installing/index.html


Also you might want a linter - if you are working in vim then a decent one is
pylint. It checks your code style. The standard is PEP8. Don;t take it too 
seriously.Install that like this, it is a bash level program not a python 
package.

  $ sudo apt install pylint
  
And go into your folder where the script is and run it like this.

  $ pylint graph_test.py
  
It should tell you about any errors. It has clear documentation of its own.
Mind you, if you use test driven development, you will not need debugging.

Finally, this approach uses in-line tests written in the same script.
That is not how Python apps or executables would normally be tested.
But it is nice and clear for our purpose.



