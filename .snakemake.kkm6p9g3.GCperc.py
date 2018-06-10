
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/ruben/anaconda/envs/snakemake-project/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05X\x10\x00\x00\x00sequenties.fastaq\x06a}q\x07X\x06\x00\x00\x00_namesq\x08}q\tsbX\x06\x00\x00\x00configq\n}q\x0bX\x07\x00\x00\x00threadsq\x0cK\x01X\x04\x00\x00\x00ruleq\rX\x06\x00\x00\x00GCpercq\x0eX\t\x00\x00\x00resourcesq\x0fcsnakemake.io\nResources\nq\x10)\x81q\x11(K\x01K\x01e}q\x12(X\x06\x00\x00\x00_coresq\x13K\x01X\x06\x00\x00\x00_nodesq\x14K\x01h\x08}q\x15(h\x13K\x00N\x86q\x16h\x14K\x01N\x86q\x17uubX\x03\x00\x00\x00logq\x18csnakemake.io\nLog\nq\x19)\x81q\x1a}q\x1bh\x08}q\x1csbX\x06\x00\x00\x00paramsq\x1dcsnakemake.io\nParams\nq\x1e)\x81q\x1f}q h\x08}q!sbX\x06\x00\x00\x00outputq"csnakemake.io\nOutputFiles\nq#)\x81q$X\n\x00\x00\x00GCperc.txtq%a}q&h\x08}q\'sbX\t\x00\x00\x00wildcardsq(csnakemake.io\nWildcards\nq))\x81q*}q+h\x08}q,sbub.')
######## Original script #########
from Bio import SeqUtils as SQ
from matplotlib import * 


seq = open(snakemake.input[0])
output = open(snakemake.output[0], "w")

header = ""
strSeq = ""

for line in seq:
    if ">" in line:
        header = line
        output.write(line + "\n")
    if line == "\n" and strSeq != "":
        GCperc = SQ.GC(strSeq)
        output.write(str(GCperc))
        hist(GCPerc, header)
        strSeq = ""
    if ">" not in line:
        strSeq += line
        
