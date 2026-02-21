from fastapi import APIRouter
from services.s3_service import get_buckets
from services.ec2_service import get_instances

router = APIRouter()

@router.get("/s3")              # Creating decorator 
def s3_bucket_info():
    """
    This function fetches the S3 buckets from the AWS
    """
    bucket_info = get_buckets()
    return bucket_info

@router.get("/ec2")
def ec2_instance_info():
    """
    fetches the list of ec2 instances on AWS
    """
    instance_info = get_instances()
    return instance_info