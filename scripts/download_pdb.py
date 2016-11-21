# this script is used to download pdb files to cwd
# python dowload_pdb.py pdb_id_1 pdb_id_2 ...etc 

import urllib # allows you to open url
from sys import argv

url = "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId="
for i in argv[1:]:
    pdbid = url+str(i)
    open( i+".pdb", "w" ).write( urllib.urlopen(pdbid).read() )
    print i+".pdb"
