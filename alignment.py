import subprocess

def align_reads(genome_dir, read_file, output_prefix):
    subprocess.run(['STAR', '--genomeDir', genome_dir, '--readFilesIn', read_file, '--outFileNamePrefix', output_prefix])

genome_dir = '/path/to/genomeDir'
read_file = '/path/to/output/file_1_trimmed.fastq'
output_prefix = '/path/to/output/file_aligned'
align_reads(genome_dir, read_file, output_prefix)
