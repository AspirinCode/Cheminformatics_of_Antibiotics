#!/usr/bin/python

from numpy import *
from sys import *
import os, sys, glob, shutil
import Tkinter

# check to see if an input file was given with a molecule list
if len(sys.argv) < 2:
   print 'Usage:'
   print './3_run_plumed.py [molecule_list]'

# set directory
dir = os.getcwd()
print dir #to test and make sure it's looking in the right place

# read through the list
file = sys.argv[1]
with open(file) as f:
   for line in f:
       molecule = line.rstrip()
       print molecule
       path = dir + '/' + molecule
       print path

       if not os.path.exists(path):
          os.makedirs(path)
       os.chdir(path)
       newcwd = os.getcwd()
       print 'current directory: ' + newcwd

       os.system('cat ' + dir + '/input/amber2xyz_tmp.tcl | sed s/MOL/' + molecule + '/g > amber2xyz.tcl')

# run vmd
       os.system('vmd -dispdev text -e amber2xyz.tcl')
# get number of atoms
       xyz = dir + '/' + molecule + '/' + molecule + '.xyz'
       g = open(xyz, "r") # open mol.xyz
       l = [] # empty list
       for lines in g:
          l.append(lines.rstrip()) # add lines to list
       g.close() # close mol.xyz
       natoms = l[0] # set natoms to first line with number of atoms
       print ""
       print natoms # print natoms

       os.system ('cat ' + dir + '/input/plumed_tmp.dat | sed -e s/NATOMS/' + natoms + '/g -e s/MOL/' + molecule + '/g > plumed.dat')

       os.system ('/home/jpc/code/plumed-2.2.0/src/lib/plumed driver --plumed plumed.dat --ixyz' + molecule + '.xyz --length-units 1.0')

# run things to calculate asphericity etc.

       stuff_to_calc = ['asphericity', 'acylindricity', 'kappa2', 'rg', 'smallest_principal_rg', 'middle_principal_rg', 'largest_principal_rg']

       for i in stuff_to_calc:
          os.system('cat ' + dir + '/input/' + i + '_tmp.gp | sed s/MOL/' + molecule + '/g > ' + molecule + '_' + i + '.gp')

# make things executable
          os.system ('chmod u+x *.gp *.tcl')

# gnuplot
          os.system ('gnuplot ' + molecule + '_' + i + '.gp')
