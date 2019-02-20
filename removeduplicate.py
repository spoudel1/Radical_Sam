#this script will remove all the duplicate sequences.
#input: fasta sequence file
#output: unique fasta sequence file

import sys

inputfile=open(sys.argv[1]).readlines()
outputfile=open(sys.argv[2],'w')

_store=[]
seqid=''
sequence=''
count=0

#checks for duplicate sequence
def dupcheck(name):
    present=0
    for x in _store:
        if name == x:
            present=1
            break
    return present

#reads the file line by line
for line in inputfile:
    line_strip=line.strip()
    if line_strip.startswith('>'):
        if count>0:
            if dupcheck(sequence)==0:
                outputfile.write(seqid+'\n'+sequence+'\n')
                _store.append(sequence)
                sequence=''
        else:
            count=count+1
        seqid=line_strip
    else:
        sequence+=line_strip
if dupcheck(sequence)==0:
    outputfile.write(seqid+'\n'+sequence+'\n')
    
