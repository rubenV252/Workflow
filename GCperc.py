from Bio import SeqUtils as SQ

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
        strSeq = ""
    if ">" not in line:
        strSeq += line
        
