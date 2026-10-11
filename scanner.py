import boto3
from minio import Minio

s3 = boto3.client(
    "s3",
    endpoint_url="http://127.0.0.1:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    region_name="us-east-1"
)

minio_client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

print("Cloud Misconfiguration Scanner")
print("--------------------------------")

response = s3.list_buckets()

for bucket in response["Buckets"]:
    bucket_name = bucket["Name"]

    print("\nBucket found:", bucket_name)

    try:
        policy = minio_client.get_bucket_policy(bucket_name)

        if '"AWS":["*"]' in policy and "s3:GetObject" in policy:
            print("WARNING: Bucket is publicly accessible!")
            print("Severity: HIGH")
            print("Issue: Anonymous users can download objects.")

        else:
            print("OK: No public object access detected.")

    except Exception as e:
        print("Could not read bucket policy:", e)