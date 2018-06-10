
######## Snakemake header ########
library(methods)
Snakemake <- setClass(
    "Snakemake",
    slots = c(
        input = "list",
        output = "list",
        params = "list",
        wildcards = "list",
        threads = "numeric",
        log = "list",
        resources = "list",
        config = "list",
        rule = "character"
    )
)
snakemake <- Snakemake(
    input = list('RNA-Seq-counts.txt'),
    output = list('Gene_id.txt'),
    params = list(),
    wildcards = list(),
    threads = 1,
    log = list(),
    resources = list(),
    config = list(),
    rule = 'isolation'
)
######## Original script #########
counts2 = function(counts,Gene_id){
  
  Var1 = read.delim2(counts,skip = 1, header = TRUE)
  Var2 = Var1$ID
  write.csv2(Var2, file = Gene_id)
}

counts2(
  snakemake@input[["counts"]],
  snakemake@output[["Gene_id"]]
)
