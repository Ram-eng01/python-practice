import boto3

ec2_client = boto3.client('ec2', region_name='ap-south-1')
x = (ec2_client.describe_volumes().get('Volumes'))

gp2_volumes = [ vol['VolumeId'] for vol in x if vol['VolumeType'] == "gp2"]



gp3_volumes = [ vol['VolumeId'] for vol in x if vol['VolumeType'] == "gp3"]

io1 = [ vol['VolumeId'] for vol in x if vol['VolumeType'] == "io1"]



print(gp2_volumes,gp3_volumes,io1)


