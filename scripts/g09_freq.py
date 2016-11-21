#!/usr/bin/python
# Compatible with python 2.7
# Reads frequency output from a g09 (gaussian) calculation
# Usage ex.: g09freq g09.log ir.dat
import sys

def ints2float(integerlist):
    for n in range(0,len(integerlist)):
        integerlist[n]=float(integerlist[n])
    return integerlist

def parse_in(infile):
    g09output=open(infile,'r')
    captured=[]
    for line in g09output:
        if ('Frequencies' in line) or ('Frc consts' in line) or ('IR Inten' in line):
            captured+=[line.strip('\n')]
    g09output.close()
    return captured

def format_captured(captured):
    vibmatrix=[]
    steps=len(captured)
    for n in range(0,steps,3):
        freqs=ints2float(filter(None,captured[n].split(' '))[2:5])
        forces=ints2float(filter(None,captured[n+1].split(' '))[3:6])
        intensities=ints2float(filter(None,captured[n+2].split(' '))[3:6])
        for m in range(0,3):
            vibmatrix+=[[freqs[m],forces[m],intensities[m]]]
    return vibmatrix

def write_matrix(vibmatrix,outfile):
    f=open(outfile,'w')
    for n in range(0,len(vibmatrix)):
        item=vibmatrix[n]
        f.write(str(item[0])+'\t'+str(item[1])+'\t'+str(item[2])+'\n')
    f.close()
    return 0

if __name__ == "__main__":
    infile=sys.argv[1]
    outfile=sys.argv[2]

    captured=parse_in(infile)

    if len(captured)%3==0:
        vibmatrix=format_captured(captured)
    else:
        print 'Number of elements not divisible by 3 (freq+force+intens=3)'
        exit()
    success=write_matrix(vibmatrix,outfile)
    if success==0:
        print 'Read %s, parsed it, and wrote %s'%(infile,outfile)
