#!/usr/bin/python

# modified script to translate gaussian output file to xyz file with optimized coordinates

from sys import argv
from glob import glob
import os

def getnoatms(file):
	for line in file:
		if 'NAtoms=' in line:
			natoms = int(line.split()[1])
			return natoms

def coordloc(file, natms):
	count = len(file)-1
	maxcount = file[count]
	while count > 0:
		if file[count].find('Number     Number       Type             X           Y           Z') != -1:
			read = count + 2
			stop = read + natms
			return read, stop
		count -= 1

def status(file):
	for i, line in enumerate(file):
		if 'Stationary point found' in file[i]:
			return 'y'
		else:
			continue

def finalE(file):
	count = len(file)-1
	maxcount = file[count]
	while count > 0:
		if file[count].find('SCF Done:') != -1:
			return file[count].split()[4]
		count -= 1

def getXYZ(file, begin_line, end_line):
	atmname = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","UUt","Fl","Uup","Lv","Uus","Uuo"]
	i = begin_line
	coords = []
	while i < end_line:
		atomline = []
		atomline.append([atmname[int(file[i].split()[1])-1],file[i].split()[3],file[i].split()[4],file[i].split()[5]])
		coords.append(atomline)
		i += 1
	return coords

def writefile(location, filename, E, coordinates):
	w = open(location + '/' + filename + '.xyz', 'w')
	w.write(str(len(coordinates)) + '\n')
	w.write(filename + '.log Final SCF Energy = ' + E + '\n')
	j = 0
	while j < len(coordinates):
		w.write('\t'.join(coordinates[j][0]) + '\n')
		j += 1
	w.close
	print location + '/' + filename + '.opt.xyz written.'

def readwrite(wd, file):
	fbase = ('.').join(str(file.split('/')[-1:]).strip("['").split('.')[:-1])
	o = open(wd + '/' + fbase + '.log', 'r').readlines()

	natms = getnoatms(o)
	coords = getXYZ(o, coordloc(o, natms)[0], coordloc(o, natms)[1])
	SCF = finalE(o)

	if status(o) == None:
		convert = raw_input(wd + '/' + fbase + '.log has not completed optimization. Convert anyway? (y/n)  ')
		if str.lower(convert) == 'y':
			writefile(wd, fbase, SCF, coords)
		else:
			pass
	else:
		writefile(wd, fbase, SCF, coords)

## Main routine

if len(argv) == 1:
	sing = 'n'
	wd = '.'
elif os.path.isdir(argv[1]):
	sing = 'n'
	wd = argv[1].strip('/')
elif os.path.isfile(argv[1]):
	sing = 'y'
	wd = '.'
	file = argv[1]

if sing == 'y':
	readwrite(wd, file)

elif sing == 'n':
	for file in glob(wd + '/*.log'):
		readwrite(wd, file)
