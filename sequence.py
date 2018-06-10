from Bio import Entrez

File = open(snakemake.input[0])
output = open(snakemake.output[0], "w")

ID = []
data = File.read()
NCBI_ID = data.split("\n")


for k in NCBI_ID:
    if k != "":
        ID.append(k)

for index in ID:
    handle = Entrez.efetch(db="gene", id=ID, rettype="gb",retmode="text")
    result = handle.read()
    
output.write(result)
output.write("\n")

