# code based on the training in pluralsight Core Python: Organizing Larger Programs

#creating packages

#modules - create a source file in sys.path
#packages - 1) create package root directory, this directory needs to be in some dir in sys.path 2) create __init__.py file in it

#--------------------------
# creating the dictory in command line
#--------------------------

#windows
type nul > demo_reader\__init__.py

#linux
mkdir demo_reader
touch demo_reader/__init__.py

#--------------------------
# checking if exists
#--------------------------
import demo_reader
type(demo_reader)

# <class 'module'>

demo_reader.__file__ 

#'/organizing-larger-programs/demo_reader/__init__.py'

#--------------------------
# PACKAGE IS A DIRECTORY CONTAINING __init__.py
#--------------------------

#create files in directory (__init__.py and multireader.py


#--------------------------
# Testing
#--------------------------

import demo_reader.multireader

r = demo_reader.multireader.MultiReader('demo_reader/__init__.py')

r.read()

# '# demo_reader/__init__.py'

r.close()

