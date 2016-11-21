#!/usr/bin/python
 
from numpy import *
from sys import *
import os, sys, glob
import Tkinter

# check to see if an input file was given with a molecule list
if len(sys.argv) < 2:
   print 'Usage:'
   print './1_params.py [molecule_list]'

# set directory

dir = os.getcwd()
print dir

file = sys.argv[1] # set file to the list of molecules
with open(file) as f:
   for line in f:
       molecule = line.rstrip()
       print molecule
       path = dir + '/' + molecule

       if not os.path.exists(path):
          os.makedirs(path)
       os.chdir(path)
       newcwd = os.getcwd()
       print 'current directory: ' + newcwd

       os.system ('cat ' + dir + '/input/mol2_to_pdb_tmp.tcl | sed s/MOL/' + molecule + '/g > mol2_to_pdb.tcl')

# vmd
       os.system ('vmd -dispdev text -e mol2_to_pdb.tcl')
       os.system ('cat ' + molecule + '.pdb | sed s/MOL/' + molecule + '/g > tmp')
       os.system ('mv tmp ' + molecule + '.pdb')

# generate pbs script for running antechamber and parmchk

       os.system(dir + '/input/param_tmp.pbs | sed -e s/MOL/' + molecule + '/g -e s/CHARGE/' + charge + '/g > param.pbs')

# make files executable
os.system ('chmod u+x *.pbs *.tcl')
