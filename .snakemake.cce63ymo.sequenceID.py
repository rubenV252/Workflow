
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/ruben/anaconda/envs/snakemake-project/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00outputq\tcsnakemake.io\nOutputFiles\nq\n)\x81q\x0b(X\x0e\x00\x00\x00Sequence.fastaq\x0cX\x0b\x00\x00\x00Afstand.txtq\re}q\x0e(h\x07}q\x0fX\x08\x00\x00\x00distanceq\x10K\x01N\x86q\x11sh\x10h\rubX\x07\x00\x00\x00threadsq\x12K\x01X\t\x00\x00\x00resourcesq\x13csnakemake.io\nResources\nq\x14)\x81q\x15(K\x01K\x01e}q\x16(h\x07}q\x17(X\x06\x00\x00\x00_nodesq\x18K\x00N\x86q\x19X\x06\x00\x00\x00_coresq\x1aK\x01N\x86q\x1buh\x18K\x01h\x1aK\x01ubX\x04\x00\x00\x00ruleq\x1cX\n\x00\x00\x00sequenceIDq\x1dX\x03\x00\x00\x00logq\x1ecsnakemake.io\nLog\nq\x1f)\x81q }q!h\x07}q"sbX\x05\x00\x00\x00inputq#csnakemake.io\nInputFiles\nq$)\x81q%X\x0c\x00\x00\x00sequence.txtq&a}q\'h\x07}q(sbX\x06\x00\x00\x00configq)}q*X\x06\x00\x00\x00paramsq+csnakemake.io\nParams\nq,)\x81q-}q.h\x07}q/sbub.')
######## Original script #########
import time
from Bio import Entrez
from tqdm import * 

File = open(snakemake.input[0])
output = open(snakemake.output[0], "w")
output1 = open(snakemake.output[1], "w")

ID = []
distance = []

for line in tqdm(File):
    if line.startswith("Annotation"):
        split = line.split(" ")
        ID.append(split[2])
        distance.append(split[3])
        time.sleep(1)
        
for index in tqdm(ID):
    handle = Entrez.efetch(db="nucleotide", id=ID, rettype="fasta", retmode="text")
    result = handle.read()
    time.sleep(1)
        
output.write(result)
output.write("\n")

for item in tqmd(distance):
    afstand = item.strip("()")
    output1.write(afstand)
    output1.write("\n")
    time.sleep(1)
