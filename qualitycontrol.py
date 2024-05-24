import subprocess

def quality_control(input_file, output_file):
    subprocess.run(['fastp', '-i', input_file, '-o', output_file, '-h', output_file + '.html'])

input_file = '/path/to/output/file_1.fastq'
output_file = '/path/to/output/file_1_trimmed.fastq'
quality_control(input_file, output_file)
