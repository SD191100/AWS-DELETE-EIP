import boto3
client = boto3.client('ec2') #  region_name='ap-south-1'
addresses = client.describe_addresses()
# print(addresses['Addresses'])

for eip in addresses['Addresses']:
    if 'NetworkInterfaceId' and 'AssociationId' not in eip:
        print(eip['PublicIp'], ': is not associated with any instance, releasing it')
        client.release_address(
            AllocationId=eip['AllocationId']
        )
