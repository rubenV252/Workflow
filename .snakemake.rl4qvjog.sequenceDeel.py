
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/ruben/anaconda/envs/snakemake-project/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x0c\x00\x00\x00sequenceDeelq\x04X\x06\x00\x00\x00outputq\x05csnakemake.io\nOutputFiles\nq\x06)\x81q\x07X\x10\x00\x00\x00sequenties.fastaq\x08a}q\tX\x06\x00\x00\x00_namesq\n}q\x0bsbX\t\x00\x00\x00wildcardsq\x0ccsnakemake.io\nWildcards\nq\r)\x81q\x0e}q\x0fh\n}q\x10sbX\x06\x00\x00\x00configq\x11}q\x12X\x06\x00\x00\x00paramsq\x13csnakemake.io\nParams\nq\x14)\x81q\x15}q\x16h\n}q\x17sbX\x05\x00\x00\x00inputq\x18csnakemake.io\nInputFiles\nq\x19)\x81q\x1a(X\x0e\x00\x00\x00Sequence.fastaq\x1bX\x0b\x00\x00\x00Afstand.txtq\x1ce}q\x1dh\n}q\x1esbX\x03\x00\x00\x00logq\x1fcsnakemake.io\nLog\nq )\x81q!}q"h\n}q#sbX\x07\x00\x00\x00threadsq$K\x01X\t\x00\x00\x00resourcesq%csnakemake.io\nResources\nq&)\x81q\'(K\x01K\x01e}q((X\x06\x00\x00\x00_coresq)K\x01h\n}q*(h)K\x00N\x86q+X\x06\x00\x00\x00_nodesq,K\x01N\x86q-uh,K\x01ubub.')
######## Original script #########
from Bio import Entrez
import time
from tqdm import *

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

for line in tqdm(File1):
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
                         
    	time.sleep(1)            
    
        
            


    
