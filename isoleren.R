input <- snakemake@input[[1]]
  
Var1 = read.delim2(input,skip = 1, header = TRUE)
Var2 = head(Var1$ID)
  
write(as.character(Var2), file = "Gene_id.txt")

Gene_id.txt <- snakemake@output[[1]]

