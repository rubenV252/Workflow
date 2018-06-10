
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/ruben/anaconda/envs/snakemake-project/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x0c\x00\x00\x00sequenceDeelq\x04X\t\x00\x00\x00resourcesq\x05csnakemake.io\nResources\nq\x06)\x81q\x07(K\x01K\x01e}q\x08(X\x06\x00\x00\x00_nodesq\tK\x01X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\x06\x00\x00\x00_coresq\rK\x01N\x86q\x0euh\rK\x01ubX\x06\x00\x00\x00configq\x0f}q\x10X\x03\x00\x00\x00logq\x11csnakemake.io\nLog\nq\x12)\x81q\x13}q\x14h\n}q\x15sbX\x07\x00\x00\x00threadsq\x16K\x01X\t\x00\x00\x00wildcardsq\x17csnakemake.io\nWildcards\nq\x18)\x81q\x19}q\x1ah\n}q\x1bsbX\x06\x00\x00\x00paramsq\x1ccsnakemake.io\nParams\nq\x1d)\x81q\x1e}q\x1fh\n}q sbX\x06\x00\x00\x00outputq!csnakemake.io\nOutputFiles\nq")\x81q#X\x10\x00\x00\x00sequenties.fastaq$a}q%h\n}q&sbX\x05\x00\x00\x00inputq\'csnakemake.io\nInputFiles\nq()\x81q)(X\x0e\x00\x00\x00Sequence.fastaq*X\x0b\x00\x00\x00Afstand.txtq+e}q,h\n}q-sbub.')
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
                         
                
    
        
            


    
