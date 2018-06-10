
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/ruben/anaconda/envs/snakemake-project/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_namesq\x08}q\t(X\x06\x00\x00\x00_coresq\nK\x00N\x86q\x0bh\x07K\x01N\x86q\x0cuh\nK\x01ubX\t\x00\x00\x00wildcardsq\rcsnakemake.io\nWildcards\nq\x0e)\x81q\x0f}q\x10h\x08}q\x11sbX\x06\x00\x00\x00outputq\x12csnakemake.io\nOutputFiles\nq\x13)\x81q\x14X\x0b\x00\x00\x00NCBI_ID.txtq\x15a}q\x16h\x08}q\x17sbX\x06\x00\x00\x00paramsq\x18csnakemake.io\nParams\nq\x19)\x81q\x1a}q\x1bh\x08}q\x1csbX\x05\x00\x00\x00inputq\x1dcsnakemake.io\nInputFiles\nq\x1e)\x81q\x1fX\x0b\x00\x00\x00Gene_id.txtq a}q!h\x08}q"sbX\x03\x00\x00\x00logq#csnakemake.io\nLog\nq$)\x81q%}q&h\x08}q\'sbX\x07\x00\x00\x00threadsq(K\x01X\x04\x00\x00\x00ruleq)X\x06\x00\x00\x00searchq*X\x06\x00\x00\x00configq+}q,ub.')
######## Original script #########
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
    
