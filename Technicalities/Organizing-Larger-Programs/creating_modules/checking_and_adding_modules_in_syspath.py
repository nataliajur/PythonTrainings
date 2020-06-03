# code based on the training in pluralsight Core Python: Organizing Larger Programs

import sys

print(sys.path)

print(sys.path[0])
print('if empty - starts Python interpreter with no arguments, and it tells to look for modules first in the current dictory')

# if you want to add a package in the directory where Python would not normally search, this is what to do

# 1st way:

# add to sys.path
import new_module

sys.path.append('name_of_directory')

import new_module

#2nd way:

#python path

#add in the shell

#windows PYTHONPATH=path1;path2;path3
#set PYTHONPATH=name_of_directory
#linux,macOs PYTHONPATH=path1:path2:path3
#export PYTHONPATH=name_of_directory

import sys

print([path for path in sys.path if 'name_of_directory' in path])

import new_module

