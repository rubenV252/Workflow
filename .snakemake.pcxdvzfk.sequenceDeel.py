
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/ruben/anaconda/envs/snakemake-project/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x0e\x00\x00\x00Sequence.fastaq\x06X\x0b\x00\x00\x00Afstand.txtq\x07e}q\x08X\x06\x00\x00\x00_namesq\t}q\nsbX\x04\x00\x00\x00ruleq\x0bX\x0c\x00\x00\x00sequenceDeelq\x0cX\t\x00\x00\x00wildcardsq\rcsnakemake.io\nWildcards\nq\x0e)\x81q\x0f}q\x10h\t}q\x11sbX\x06\x00\x00\x00paramsq\x12csnakemake.io\nParams\nq\x13)\x81q\x14}q\x15h\t}q\x16sbX\x03\x00\x00\x00logq\x17csnakemake.io\nLog\nq\x18)\x81q\x19}q\x1ah\t}q\x1bsbX\x07\x00\x00\x00threadsq\x1cK\x01X\x06\x00\x00\x00configq\x1d}q\x1eX\x06\x00\x00\x00outputq\x1fcsnakemake.io\nOutputFiles\nq )\x81q!X\x10\x00\x00\x00sequenties.fastaq"a}q#h\t}q$sbX\t\x00\x00\x00resourcesq%csnakemake.io\nResources\nq&)\x81q\'(K\x01K\x01e}q((X\x06\x00\x00\x00_coresq)K\x01X\x06\x00\x00\x00_nodesq*K\x01h\t}q+(h*K\x00N\x86q,h)K\x01N\x86q-uubub.')
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
    
        
            


    
