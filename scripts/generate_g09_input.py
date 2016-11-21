#!/usr/bin/python

# modified script to generate submission file for newton for gaussian jobs

from sys import argv, exit
from glob import glob
from os import getcwd, system, path
from datetime import datetime

## Gathering user input
if len(argv) != 3:
        print "Usage: [Script.py] [# Procs] [Queue (-l, -m, -s)]"
	exit()

nprocs = argv[1]
queue = argv[2]

if queue == '-l':									# Long queue - unlimited time
	q = '-q long*'
elif queue == '-m':								# medium queue - 24h time limit
	q = '-q medium*'
elif queue == '-s':								# short queue - 2h time limit
	q = '-q short*'

## Gathering information for all jobs
for file in sorted(glob("./*.com")):
	fbase = '.'.join(path.basename(file).split('.')[:-1])

	## Generating lines of the SGE script
	flines = []
	flines.append([str('#!/bin/bash -l') + '\n'])
	flines.append([str('#$ -S /bin/bash') + '\n'])
	flines.append([str('#$ -cwd') + '\n'])
	flines.append([str('#$ -N ' + fbase) + '\n'])
	flines.append([str('#$ ' + q) + '\n'])
	flines.append([str('#$ -pe threads ' + nprocs) + '\n'])
	flines.append(['\n'])
	flines.append([str('mol="' + fbase + '"') + '\n'])
	flines.append(['\n'])
	flines.append([str('SCRATCH=/lustre/scratch/$USER ; export SCRATCH') + '\n'])
	flines.append([str('mkdir -p $SCRATCH/$JOB_ID') + '\n'])
	flines.append([str('cd $SCRATCH/$JOB_ID') + '\n'])
	flines.append(['\n'])
	flines.append([str('module load gaussian/g09') + '\n'])
	flines.append(['\n'])
	flines.append([str('g09 $SGE_O_WORKDIR/$mol.com > $SGE_O_WORKDIR/$mol.log') + '\n'])
	flines.append(['\n'])
	flines.append([str('mv $mol.chk $SGE_O_WORKDIR') + '\n'])
	flines.append(['\n'])
	flines.append([str('cd $SGE_O_WORKDIR') + '\n'])
	flines.append(['\n'])
	flines.append([str('/bin/rm -rf $SCRATCH/$JOB_ID') + '\n'])

## Writing lines of SGE script to file
	w = open(fbase + '.sge', 'w')
	for line in flines:
		w.writelines('\t'.join(line))
	print fbase + '.sge written.'
