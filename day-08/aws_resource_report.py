# Part 1 – AWS Automation using Python (Boto3)

import boto3
import json

def get_connections(service):
    return boto3.client(service, region_name = "us-east-1")

def show_instances(ec2_client):
    response = ec2_client.describe_instances()

    # print(boto3.Session().region_name)    # gives the default region boto3 connecting to 
    # print(response)       # used to check what response we are getting and then fetching the important data

    instance_list = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_list.append({
                "InstanceId": instance["InstanceId"],
                "State": instance["State"]["Name"]
            })

    return instance_list

            
def show_buckets(s3_client):
    response = s3_client.list_buckets()

    bucket_list = []
    for bucket in response["Buckets"]:
        if "Name" in bucket:
            bucket_list.append(bucket["Name"])

    return bucket_list

def write_json(s3_client,ec2_client):
    bucket_name = show_buckets(s3_client) 
    instances = show_instances(ec2_client)

    data = {
    "buckets": bucket_name,
    "instances": instances
}


    with open("day-08/output.json","w") as f:
        json.dump(data, f , indent = 4)


s3 = get_connections("s3")
print("S3 buckets are:")
buckets = show_buckets(s3)
for b in buckets:
    print(b)

ec2 = get_connections("ec2")
print("\nEC2 instance Details:")
instances = show_instances(ec2)
for i in instances:
    print("InstanceId:", i["InstanceId"], "State:", i["State"])

write_json(s3,ec2)