
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/ruben/anaconda/envs/snakemake-project/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05X\x10\x00\x00\x00sequenties.fastaq\x06a}q\x07X\x06\x00\x00\x00_namesq\x08}q\tsbX\x04\x00\x00\x00ruleq\nX\x0c\x00\x00\x00sequenceDeelq\x0bX\x05\x00\x00\x00inputq\x0ccsnakemake.io\nInputFiles\nq\r)\x81q\x0e(X\x0e\x00\x00\x00Sequence.fastaq\x0fX\x0b\x00\x00\x00Afstand.txtq\x10e}q\x11h\x08}q\x12sbX\x07\x00\x00\x00threadsq\x13K\x01X\x03\x00\x00\x00logq\x14csnakemake.io\nLog\nq\x15)\x81q\x16}q\x17h\x08}q\x18sbX\x06\x00\x00\x00configq\x19}q\x1aX\t\x00\x00\x00wildcardsq\x1bcsnakemake.io\nWildcards\nq\x1c)\x81q\x1d}q\x1eh\x08}q\x1fsbX\t\x00\x00\x00resourcesq csnakemake.io\nResources\nq!)\x81q"(K\x01K\x01e}q#(X\x06\x00\x00\x00_nodesq$K\x01h\x08}q%(h$K\x00N\x86q&X\x06\x00\x00\x00_coresq\'K\x01N\x86q(uh\'K\x01ubX\x06\x00\x00\x00paramsq)csnakemake.io\nParams\nq*)\x81q+}q,h\x08}q-sbub.')
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
        distance += 2
        output.write("\n")
        output.write(line + punten[distance] + ".." + punten[distance + 1])
        output.write("\n")
    if ">" not in line:
        for letter in line:
            count += 1
            if count >= int(punten[distance]) and count <= int(punten[distance +1]):
                output.write(letter)
                if count = int(punten[distance + 1]):
                    count = 0         
                
    
        
            


    
