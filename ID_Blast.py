from Bio import TogoWS

def blast(Gene_id, Blast_data):

    ID = []
    i = 0

    file1 = open(Gene_id, "r")
    file2 = open(Blast_data, "w")

    for k in file1:
            ID.append(k)

    while i != len(ID):
        for id in TogoWS.search_iter("gene", ID[i], limit=1):
            file2.write(id)
            i += 1

blast(snakemake.input[0],
      snakemake.output[0])
