#!/usr/bin/python
import boto3 
ec2 = boto3.resource('ec2', region_name='us-west-2')

#filters = [{ 'name': 'InstanceStatus', 'value': ''}]
#instances = ec2.instances.filter(Filters)

#for instance in ec2.meta.client.describe_instance_status()['InstanceStatuses': name]:
#   print(instance)

print "\nPrinting Public IP and Instance Name:"
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.public_ip_address, instance.tags[0].get("Value"))

simples = ec2.instances.all()
#attrs = vars(simples)
print "\nPrinting Simples:"
print 

print "\nPrinting ID, Public IP and \"ec2.instances.all()\""
for simple in simples:
    print simple.id, simple.public_ip_address, simple.items()

print "\nPrinting meta tags"
#for status in ec2.meta.client.describe_instance_status()['InstanceStatuses': name]:
 #   print status

