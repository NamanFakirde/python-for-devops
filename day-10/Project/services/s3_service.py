# script to get the S3 service info

import boto3

def get_buckets():
    """
    fetches the list of buckets from the AWS console 
    """
    s3_client = boto3.client("s3")
    buckets = s3_client.list_buckets()["Buckets"]

    list_bucket = []
    for bucket in buckets:

        bucket_name = bucket["Name"]
        list_bucket.append(bucket_name)

    return {
        "total buckets": len(list_bucket),
        "buckets": list_bucket
    }