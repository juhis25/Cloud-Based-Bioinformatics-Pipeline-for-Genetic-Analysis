import subprocess

def variant_calling(reference_genome, input_bam, output_vcf):
    subprocess.run(['gatk', 'HaplotypeCaller', '-R', reference_genome, '-I', input_bam, '-O', output_vcf])

reference_genome = '/path/to/reference/genome.fasta'
input_bam = '/path/to/output/file_aligned.bam'
output_vcf = '/path/to/output/file_variants.vcf'
variant_calling(reference_genome, input_bam, output_vcf)
