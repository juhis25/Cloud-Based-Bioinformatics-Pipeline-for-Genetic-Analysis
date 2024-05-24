import boto3

def create_ec2_instance():
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-0abcdef1234567890',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='your-key-pair-name'
    )
    print(f'Created instance with ID: {instance[0].id}')

create_ec2_instance()
