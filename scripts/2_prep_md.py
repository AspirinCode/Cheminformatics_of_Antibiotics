#!/usr/bin/python

from numpy import *
from sys import *
import os, sys, glob, shutil
import Tkinter

# check to see if an input file was given with a molecule list
if len(sys.argv) < 2:
   print 'Usage:'
   print './2_prep_md.py [molecule_list] [bcc]'
   print 'Use bcc param if you want to use antechamber to generate AM1-BCC charges.'
   print 'Otherwise charges from MOL_mk.prep will be used as default.'

# set directory
dir = os.getcwd()

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

# copy over pdb file...
#       shutil.copy2(dir + '/to_do/' + molecule + '.pdb', dir + '/' + molecule)
#       print 'copied to_do ' + molecule + '.pdb to ' + dir + '/' + molecule

# look for inpcrd file
       if not os.path.exists(dir + '/' + molecule + '/' +  molecule + '.inpcrd'):
          print 'no inpcrd file found'
	  if len(sys.argv) > 1:
	     os.system('cat ' + dir + '/input/leap.script_bcc.tmp | sed s/MOL/' + molecule + '/g > ' + dir + '/' + molecule + '/leap.script')
          else:
             os.system('cat ' + dir + '/input/leap.script.tmp | sed s/MOL/' + molecule + 'g > ' + dir + '/' + molecule + '/leap.script')

             os.system('$AMBERHOME/bin/tleap -s -f leap.script')

# copy over .in files from input directory
       to_copy = ['min.in', 'equil.in', 'equil2.in', 'prod.in']
       for j in to_copy:
          shutil.copy2(dir + '/input/' + j, dir + '/' + molecule)
          print "copied input/" + j + ' to '+  dir + '/' + molecule

       os.system('cat ' + dir + '/input/equil_tmp.pbs | sed s/MOL/' + molecule + '/g > equil.pbs')
       os.system('cat ' + dir + '/input/gpu_tmp.pbs | sed s/MOL/' + molecule + '/g > gpu.pbs')

# make executable
os.system ('chmod u+x *.pbs')
