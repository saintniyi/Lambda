1.  Navigate to "LambdaMiniProject" directory and execute "init.sh" with 
    the command: ./init.sh to prepare and set up the environment

2.  activate virtual environment: source ./sandbox2/bin/activate

3.  execute "run.sh" with ./run.sh to trigger run.py that will get data 
    from db and save to s3 bucket. Confirm file is in the s3 bucket

4.  Navigate to "lambda_script" folder and from the folder, execute:  
    "pip install requests"

5.  In the "lambda_script" folder, execute: "local_lambda_test.py" using 
    the command: python ./local_lambda_test.py, if it works, you will see the file saved to s3 bucket in step 3 now downloaded to "lambda_script" folder
    and a 201 response status code

6.  The code in "local_lambda_test.py" was used to prepare the   
    "lambda_function.py" script used to run aws lambda function.

7   Navigate to "LambdaMiniProject" folder and from the folder, execute 
    "mklayer.sh" file with the command ./mklayer.sh, this will setup "my-lambda-layer",  "aws-layer" and lambda-layer.zip"

8.  Upload the lambda-layer.zip file to aws as a lambda layer

9.  Copy the "lambda_function.py" code to a lambda function in aws

10. Test the code to ensure that when an uploads to s3 bucket occur, a lambda 
    function will be triggered to download the file from the same s3 bucket and post it a url, if the lambda fuction succeeeds, you will get a status 201 response