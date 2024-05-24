import boto3

def upload_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name or file_name)
    except Exception as e:
        print(f"Error uploading file: {e}")

file_name = '/path/to/output/SRR12345678_variants.vcf'
bucket = 'your-s3-bucket'
upload_to_s3(file_name, bucket)
