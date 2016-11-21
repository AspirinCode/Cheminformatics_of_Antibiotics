#!/usr/bin/python

# python script to generate gaussian09 optimization input files for each molecule in a list

from sys import *
import os, sys, glob, shutil
import string, csv

# check to see if an input file was given with a molecule list
if len(sys.argv) != 2:
   print 'Usage:'
   print './1_qm_opt.py [molecule_list]'

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

       shutil.copy(dir + '/files/xyz/' + molecule + '.xyz', newcwd)

       flines = []
       flines.append([str('%nproc=12') + '\n' ])
       flines.append([str('%Mem=2GB') + '\n'])
       flines.append([str('# B3LYP/6-31G(d,p) symmetry=none scf(conver=8) opt(VeryTight) Int=UltraFine SCRF=(PCM,Solvent=Water)') + '\n'])
       flines.append(['\n'])
       flines.append([str(molecule)] + [str('.b3lyp.631gdp.opt') + '\n'])
       flines.append(['\n'])
       flines.append([str('0 1') + '\n'])

       flines.append(['\n'])
       flines.append([str('H C O N F 0') + '\n'])
       flines.append([str('6-31+G(d,p)') + '\n'])
       flines.append([str('****') + '\n'])
       flines.append(['\n'])

# write to file
       to_file = open(molecule + '.b3lyp.631gdp.opt.com', 'w')
       for line in flines:
           to_file.writelines('\t'.join(line))
       print molecule + '.b3lyp.631gd.opt.com written.'
