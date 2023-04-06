import boto3
import pyspark

s3_resource = boto3.resource('s3')

test = s3_resource.Object(bucket_name='ramatestbucket04', key='sample.txt').get()['Body'].read().decode('utf-8').splitlines()

print(test)
