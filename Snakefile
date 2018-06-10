rule all:
    input:"PubMedID.txt","sequenties.fasta","GCperc.txt" 
    shell: "snakemake --dag | dot -Tsvg > dag.svg"
          
rule isolation:    
    input:  "RNA-Seq-counts.txt"
    output: "Gene_id.txt"	    
    script: "isoleren.R"

rule search:
   input: "Gene_id.txt"
   output: "NCBI_ID.txt"
   script: "kegg-search.py"

rule sequence:
   input: "NCBI_ID.txt"
   output: "sequence.txt"
   script: "sequence.py"

rule sequenceID:
   input: "sequence.txt"
   output: "Sequence.fasta", distance = "Afstand.txt"
   script: "sequenceID.py"

rule sequenceDeel:
   input: "Sequence.fasta", "Afstand.txt"
   output: "sequenties.fasta"
   script: "sequenceDeel.py"

rule pubmedID:
   input: "NCBI_ID.txt"
   output: "PubMedID.txt"
   script: "Pubmed_id.py"

rule GCperc:
   input: "sequenties.fasta"
   output: "GCperc.txt"
   script: "GCperc.py"



