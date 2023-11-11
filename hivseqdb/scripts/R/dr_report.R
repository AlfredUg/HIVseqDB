args <- commandArgs(trailingOnly = TRUE)
json_file=args[1]
output_dir=args[2]

print(json_file)
print(output_dir)

generate_dr_report<-function(path){
    hivdr <- jsonlite::fromJSON(path, flatten = TRUE)
    tmp<-data.frame()
    for (i in 1:dim(hivdr)[1]) {
    seq_df <- hivdr[i,]
    seq<-seq_df$inputSequence.header
    drug_res<-seq_df$drugResistance[[1]]
    genes<-drug_res$gene.name
    for (gene in unique(genes)) {
        gene_df<-drug_res[drug_res$gene.name==gene,]
        # extracted the version and date
        version <- gene_df$version.text
        verDate <- gene_df$version.publishDate
        gene_drug_scores<-gene_df$drugScores[[1]]
        gene_drug_scores<-gene_drug_scores[c("drugClass.name","drug.name", "score", "text")]
        tmp<-rbind(tmp, gene_drug_scores)
        }
    names(tmp)<-c("drugClass.name", "Drug name", "HIVDB Score", "Drug susceptibility")
    mutations<-seq_df$alignedGeneSequences[[1]]$mutations
    subtype<-hivdr$subtypeText
    AApositions<-hivdr[[3]][[1]]
    AApositions<-AApositions[c("firstAA","lastAA","gene.name")]
    drugScores_comments<-hivdr$drugResistance[[1]]$drugScores
    }
    out<-list(seq=seq, genes=genes, drugscores=tmp, mutations=mutations, version=version, version_date=verDate, subtype=subtype,AApositions=AApositions,comments=drugScores_comments)
    return(out)
}

hivdr<-generate_dr_report(json_file)
seq<-hivdr$seq
seq<-sub("_.*","",hivdr$seq)
genes<-hivdr$genes
mutations<-hivdr$mutations
tmp<-hivdr$drugscores
AApositions<-hivdr$AApositions
comments<-hivdr$comments
tmp$sample_ID<-seq
write.csv(tmp, file=paste0(output_dir,"/",seq,"_drugscores.csv"), quote=FALSE, row.names=FALSE)
