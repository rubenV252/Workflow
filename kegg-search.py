from Bio import Entrez
import re

file1 = open(snakemake.input[0])
file2 = open(snakemake.output[0], "w")
ID = []
searchList = []

data = file1.read()
accessie = data.split("\n")

for AC in accessie:
    if AC != "":
        ID.append(AC)

for index in ID:
    Entrez.email = "ruben.vermaas1@gmail.com"
    request = Entrez.esearch(db="gene",term=index)
    result = Entrez.read(request)
    request.close()
    print("record: ", result)

    searchID = (result["IdList"])
    print("NCBI searchID: ", searchID)
    searchList.append(searchID)
    strSearch = str(searchID)
    NCBI_ID = strSearch.strip("['']")
    
    file2.write(NCBI_ID)
    file2.write("\n")
    snakemake.output[0] = file2
    
