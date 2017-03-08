#!/usr/bin/python
import boto3 
ec2 = boto3.resource('ec2', region_name='us-west-2')

### Print Running Instances
print "\nPrinting Public IP and Instance Names of Running Instances:"
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
#  print(instance.public_ip_address, instance.tags[0].get("Value"))
  print instance.tags[0]['Value'], "\t", instance.public_ip_address, "\t", instance.security_groups[0]['GroupId']
  print instance.tags[1].get("Value")





#print "\n\n\n### Printing ID, Public IP and Security Group" 
#simples = ec2.instances.all()
#for simple in simples:
#  print simple.tags[0]['Value'], simple.public_ip_address, simple.security_groups[0]['GroupId']


