
# This script uses quasitools and sierralocal for HIV drug resistance analysis of short read data 

# Specify inputs to quasitools HyDRA 
input=$1 # location of the input FASTQ files
output=$2 # location where files generated during the analysis will be stored
consensus_Percentage=$3
error_Rate=$4
length_Cutoff=$5
minimum_Allele_Count=$6
minimum_Mutation_Frequency=$7
minimum_Read_Depth=$8
minimum_Variant_Quality=$9
score_Cutoff=${10}

# Iterate over the samples and run quastiools and HyDRA on short read data
for sample in $(ls $input/*_1.fastq); do
    # pick the basename of the forward read file name - which is basically the sample name 
    bn=$(basename $sample '_1.fastq');
    # run quasitools on the paired-end data
    quasitools hydra $input/${bn}_1.fastq $input/${bn}_2.fastq --consensus_pct ${consensus_Percentage} --error_rate ${error_Rate} --length_cutoff ${length_Cutoff} --min_ac ${minimum_Allele_Count} --reporting_threshold ${minimum_Mutation_Frequency} --min_dp ${minimum_Read_Depth} --min_variant_qual ${minimum_Variant_Quality} --score_cutoff ${score_Cutoff} --generate_consensus --output_dir $output;
    # move outputs to appropriate output directories
    mv $output/consensus.fasta $output/${bn}_consensus.fasta 
    mv $output/dr_report.csv $output/${bn}_dr_report.csv
    mv $output/mutation_report.aavf $output/${bn}_mutation_report.aavf
    # run sierralocal on the consensus sequence for drug resistance interpretation
    sierralocal $output/${bn}_consensus.fasta -o $output/${bn}.json  
    # process JSON file to produce tabular outputs which will later be populated in the database
    Rscript scripts/R/dr_report.R $output/${bn}.json $output
    # remove intermediate files (alignment and variant call files) to free up some disk space
    rm $output/align.bam $output/align.bam.bai $output/*.fastq $output/*.vcf    
done

# combine all drug score outputs into a single file
cat $output/*_drugscores.csv > $output/tmp_hivdr_report.csv
grep -v "Drug" $output/tmp_hivdr_report.csv > $output/combined_hivdr_report.csv
# add sample names to minority resistant variants output files 
for f in $(ls $output/*dr_report.csv); do bn=$(basename $f '_dr_report.csv'); sed "s/$/,$bn/g" $f >  $output/${bn}_renamed_report.csv; done
# merge all minority resistant variants output files  into a single file
cat $output/*_renamed_report.csv > $output/tmp_minority_variants_report.csv
# each sample has a header line in the merged file, so we remove the header line 
grep -v "Chromosome" $output/tmp_minority_variants_report.csv > $output/combined_minority_variants_report.csv