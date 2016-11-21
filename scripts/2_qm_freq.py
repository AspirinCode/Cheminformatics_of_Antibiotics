#!/usr/bin/python
# generate gaussian09 frequency calculation input file on newton to check for negative frequencies in optimized structure

from sys import *
import os, sys, glob, shutil
import string, csv

# check to see if an input file was given with a molecule list
if len(sys.argv) != 2:
   print 'Usage:'
   print './2_qm_freq.py [molecule_list]'

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

       shutil.copy(dir + '/files/xyz/' + molecule + '.b3lyp.631gdp.opt.xyz', newcwd)

       charges = ['chelpg', 'hf631gd.mk', 'mk']
       for charge in charges:
          flines = []
          flines.append([str('%nproc=12') + '\n' ])
          flines.append([str('%Mem=2GB') + '\n'])

          if charge == 'chelpg':
             flines.append([str('#P B3LYP/6-31G(d,p) symmetry=none scf(conver=8) Int=UltraFine Pop=CHelpG IOP(6/33=2)') + '\n'])
          elif charge == 'hf631gd.mk':
             flines.append([str('#P HF/6-31G(d) symmetry=none scf(conver=8) Int=UltraFine Pop=MK IOP(6/33=2)') + '\n'])
          elif charge == 'mk':
             flines.append([str('#P B3LYP/6-31G(d,p) symmetry=none scf(conver=8) Int=UltraFine Pop=MK IOP(6/33=2)')  + '\n'])

          flines.append(['\n'])
          flines.append([str(molecule) + '.' + str(charge) + '\n'])
          flines.append(['\n'])
          flines.append([str('0 1') + '\n'])

          flines.append(['\n'])
          flines.append([str('H C O N F 0') + '\n'])
          flines.append([str('6-31+G(d,p)') + '\n'])
          flines.append([str('****') + '\n'])
          flines.append(['\n'])

# write to file
          to_file = open(molecule + '.' + charge + '.com', 'w')
          for line in flines:
             to_file.writelines('\t'.join(line))
          print molecule + '.' + charge + '.com written.'
