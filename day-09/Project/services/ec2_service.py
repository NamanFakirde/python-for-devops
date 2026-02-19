# script to get the ec2 instance info

import boto3

def get_instances():
    """
    Docstring to get the instances fom the AWS console
    """
    ec2_client = boto3.client("ec2", region_name = "us-east-1")     # change the region as per requirement
    response = ec2_client.describe_instances()
    
    # print(response["Reservations"])   # helps to fetch the details
    
    instance_details = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_details.append({
                "InstanceId": instance["InstanceId"],
                "State": instance["State"]["Name"]
            })
    return instance_details

get_instances()