import boto3


def get_client():
    return boto3.client('s3')


def list_s3_buckets():
    s3 = get_client()
    response = s3.list_buckets()
    for bucket in response.get('Buckets'):
        yield bucket['Name']


def list_s3_objects(bucket):
    s3 = get_client()
    response = s3.list_objects(Bucket=bucket)['Contents']
    for resp in response:
        yield resp["Key"]


nik = list_s3_buckets()
list_s3_objects(nik)
