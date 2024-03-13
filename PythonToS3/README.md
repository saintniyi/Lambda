1. set all secrets in .env
2. set all config in config.toml
3. run **init.sh** to create a virtual environment
4. the python script enbeded in **run.sh**, and use **run.sh**  to control job
5. there are two versions of python script:
    - run_v1.py: This version uses boto3 and aws key and secrets, the version can be used in any platform any condition.
    - run_v2.py: This is a version for scripts running on AWS EC2. Because we grant the EC2 a IAM role to access the S3, therefore, secrets and boto3 are not required. 
