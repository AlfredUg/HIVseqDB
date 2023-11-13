
input=$1
output=$2
min_freq=$3
min_dp=$4
consensus_pct=$5
error_rate=$6
length=$7
allele_count=$8 
variant_qual=$9
score=$10
read_quality=$11

for sample in $(ls $input/*_1.fastq); do
    bn=$(basename $sample '_1.fastq');
    
    quasitools hydra $input/${bn}_1.fastq $input/${bn}_2.fastq \
     --reporting_threshold ${min_freq} \
     --min_dp ${min_dp} \
     --consensus_pct ${consensus_pct} \
     --error_rate ${error_rate} \
     --length_cutoff ${length} \
     --min_ac ${allele_count} \
     --min_variant_qual ${variant_qual} \
     --score_cutoff ${score} \
     --min_read_qual ${read_quality} \
     --generate_consensus \
     -o $output;

    mv $output/consensus.fasta $output/${bn}_consensus.fasta 
    mv $output/dr_report.csv $output/${bn}_raw_report.csv
    sed "s/$/,$bn/g" $output/${bn}_raw_report.csv > $output/${bn}_dr_report.csv
    mv $output/mutation_report.aavf $output/${bn}_mutation_report.aavf
    sierralocal $output/${bn}_consensus.fasta -o $output/${bn}.json
    Rscript scripts/R/dr_report.R $output/${bn}.json $output  
    rm $output/align.bam $output/align.bam.bai $output/*.fastq $output/*.vcf    
done

cat $output/*_drugscores.csv > $output/tmp_hivdr_report.csv
grep -v "Drug" $output/tmp_hivdr_report.csv > $output/combined_hivdr_report.csv

cat $output/*_dr_report.csv > $output/tmp_minority_variants_report.csv
grep -v "Chromosome" $output/tmp_minority_variants_report.csv > $output/combined_minority_variants_report.csv
