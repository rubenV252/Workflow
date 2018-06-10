
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/ruben/anaconda/envs/snakemake-project/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_coresq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x08K\x00N\x86q\x0bh\x07K\x01N\x86q\x0cuubX\x06\x00\x00\x00outputq\rcsnakemake.io\nOutputFiles\nq\x0e)\x81q\x0fX\x10\x00\x00\x00sequenties.fastaq\x10a}q\x11h\t}q\x12sbX\x04\x00\x00\x00ruleq\x13X\x0c\x00\x00\x00sequenceDeelq\x14X\x03\x00\x00\x00logq\x15csnakemake.io\nLog\nq\x16)\x81q\x17}q\x18h\t}q\x19sbX\x06\x00\x00\x00configq\x1a}q\x1bX\t\x00\x00\x00wildcardsq\x1ccsnakemake.io\nWildcards\nq\x1d)\x81q\x1e}q\x1fh\t}q sbX\x07\x00\x00\x00threadsq!K\x01X\x05\x00\x00\x00inputq"csnakemake.io\nInputFiles\nq#)\x81q$(X\x0e\x00\x00\x00Sequence.fastaq%X\x0b\x00\x00\x00Gene_id.txtq&e}q\'h\t}q(sbX\x06\x00\x00\x00paramsq)csnakemake.io\nParams\nq*)\x81q+}q,h\t}q-sbub.')
######## Original script #########
from Bio import Entrez

File1 = open(snakemake.input[0])
File2 = open(snakemake.input[1])
output = open(snakemake.output[0], "w")

data = File2.read()
data = data.replace("\n", "..")
data = data.replace(")", "(")
data = data.replace("(", "")

count = 0
distance = -2

punten = data.split("..")
punten = list(filter(None, punten))

for line in File1:
    if ">" in line:
        line = line.replace("\n", " ")
        count = 0
        distance += 2
        output.write("\n")
        output.write(line + punten[distance] + ".." + punten[distance + 1])
        output.write("\n")
    if ">" not in line:
        for letter in line:
            count += 1
            if count >= int(punten[distance]) and count <= int(punten[distance +1]):
                output.write(letter)
                         
                
    
        
            


    
