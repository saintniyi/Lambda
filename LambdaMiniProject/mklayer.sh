#!/bin/bash

# In dev enviroment, execute this file in LambdaMiniProject directory

echo "removing existing my-lambda-layer directory"
rm  -rf my-lambda-layer

echo "creating new my-lambda-layer directory"
mkdir my-lambda-layer

echo "creating runtime libraries"
cp ./requirements.txt  ./my-lambda-layer
cd my-lambda-layer/
mkdir -p aws-layer/python/lib/python3.9/site-packages
pip3 install -r requirements.txt --target aws-layer/python/lib/python3.9/site-packages
cd aws-layer

echo "Generating layer zip file"
zip -r9 lambda-layer.zip .

echo "successfully completed creating zip layer"