#!/usr/bin/python
import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
	if bucket.name.endswith("trail"):
		print(bucket)
	if bucket.name.startswith("ryanp"):
		print(bucket.name)
		


