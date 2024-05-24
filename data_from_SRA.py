import subprocess

def download_sra_data(sra_id, output_dir):
    subprocess.run(['prefetch', sra_id, '-O', output_dir])
    subprocess.run(['fasterq-dump', '--split-files', '--outdir', output_dir, sra_id])

sra_id = 'SRR7225813', 'SRR7225812'
output_dir = '/path/to/output'
download_sra_data(sra_id, output_dir)
