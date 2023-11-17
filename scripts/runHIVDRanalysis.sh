
input=$1
output=$2
consensus_Percentage=$3
error_Rate=$4
length_Cutoff=$5
minimum_Allele_Count=$6
minimum_Mutation_Frequency=$7
minimum_Read_Depth=$8
minimum_Variant_Quality=$9
score_Cutoff=${10}

for sample in $(ls $input/*_1.fastq); do
    bn=$(basename $sample '_1.fastq');
    quasitools hydra $input/${bn}_1.fastq $input/${bn}_2.fastq --consensus_pct ${consensus_Percentage} --error_rate ${error_Rate} --length_cutoff ${length_Cutoff} --min_ac ${minimum_Allele_Count} --reporting_threshold ${minimum_Mutation_Frequency} --min_dp ${minimum_Read_Depth} --min_variant_qual ${minimum_Variant_Quality} --score_cutoff ${score_Cutoff} --generate_consensus --output_dir $output;
    mv $output/consensus.fasta $output/${bn}_consensus.fasta 
    mv $output/dr_report.csv $output/${bn}_dr_report.csv
    mv $output/mutation_report.aavf $output/${bn}_mutation_report.aavf
    sierralocal $output/${bn}_consensus.fasta -o $output/${bn}.json  
    Rscript scripts/R/dr_report.R $output/${bn}.json $output
    rm $output/align.bam $output/align.bam.bai $output/*.fastq $output/*.vcf    
done

cat $output/*_drugscores.csv > $output/tmp_hivdr_report.csv
grep -v "Drug" $output/tmp_hivdr_report.csv > $output/combined_hivdr_report.csv

cat $output/*_dr_report.csv > $output/tmp_minority_variants_report.csv
grep -v "Chromosome" $output/tmp_minority_variants_report.csv > $output/combined_minority_variants_report.csv
