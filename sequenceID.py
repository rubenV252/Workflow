import time
from Bio import Entrez
from tqdm import * 

File = open(snakemake.input[0])
output = open(snakemake.output[0], "w")
output1 = open(snakemake.output[1], "w")

ID = []
distance = []

for line in File:
    if line.startswith("Annotation"):
        split = line.split(" ")
        ID.append(split[2])
        distance.append(split[3])
       
        
for index in tqdm(ID):
    handle = Entrez.efetch(db="nucleotide", id=ID, rettype="fasta", retmode="text")
    result = handle.read()
    time.sleep(1)
        
output.write(result)
output.write("\n")

for item in distance:
    afstand = item.strip("()")
    output1.write(afstand)
    output1.write("\n")
    
