
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/ruben/anaconda/envs/snakemake-project/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_coresq\x07K\x01X\x06\x00\x00\x00_namesq\x08}q\t(h\x07K\x00N\x86q\nX\x06\x00\x00\x00_nodesq\x0bK\x01N\x86q\x0cuh\x0bK\x01ubX\x06\x00\x00\x00configq\r}q\x0eX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11}q\x12h\x08}q\x13sbX\x03\x00\x00\x00logq\x14csnakemake.io\nLog\nq\x15)\x81q\x16}q\x17h\x08}q\x18sbX\x06\x00\x00\x00outputq\x19csnakemake.io\nOutputFiles\nq\x1a)\x81q\x1bX\x10\x00\x00\x00sequenties.fastaq\x1ca}q\x1dh\x08}q\x1esbX\x04\x00\x00\x00ruleq\x1fX\x0c\x00\x00\x00sequenceDeelq X\x05\x00\x00\x00inputq!csnakemake.io\nInputFiles\nq")\x81q#(X\x0e\x00\x00\x00Sequence.fastaq$X\x0b\x00\x00\x00Afstand.txtq%e}q&h\x08}q\'sbX\x07\x00\x00\x00threadsq(K\x01X\t\x00\x00\x00wildcardsq)csnakemake.io\nWildcards\nq*)\x81q+}q,h\x08}q-sbub.')
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
                       
                
    
        
            


    
