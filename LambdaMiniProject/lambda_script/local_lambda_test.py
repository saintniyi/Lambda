#########################################################
###This is the version test on local server##############
#########################################################


import requests
import pandas as pd
import json 
import sqlalchemy as db
from dotenv import load_dotenv
from datetime import date
import os
import toml 
import subprocess


def mysql_connect(host, user, password, database, port,schema):
    """
    Connect to the database
    """
    engine = db.create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')
    return engine

def get_customer_id(cusid_file):
    """
    Read customer_id_file and return a string list of customer_id
    """
    li=[]
    with open(cusid_file,'rb') as f:
        data = json.load(f)
        for value in data["customerID"].values():
            li.append(str(value))
        
    id_string = "("+ ",".join(li)+")"
    return id_string

def get_customer_data(engine, sql):
    """
    Get customer data from database
    """
    mysql_result = engine.execute(sql)
    records=[]
    for row in mysql_result:
        doc={"id":row[0], "name":row[1], "date":date.today().strftime('%Y-%m-%d')}
        records.append(doc)
    data=json.dumps(records)
    return data

def get_customer_data_pandas(engine, sql):
    """
    Get customer data from database with pandas way
    """
    df=pd.read_sql(sql, con=engine)
    data=df.to_json(orient='records')
    return data


if __name__=="__main__": 
    app_config = toml.load('config.toml')
    
    api_url = app_config['api']['api_url']
    
    host=app_config['db']['host']
    port=app_config['db']['port']
    database=app_config['db']['database']
    schema=app_config['db']['schema']

    bucket=app_config['s3']['bucket']
    folder=app_config['s3']['folder']

    load_dotenv()
    user=os.getenv('user')
    password=os.getenv('password')

    # copy customer file from bucket: my-load-bucket/input to "lambda_script" local folder
    subprocess.call(['aws','s3','cp',f's3://{bucket}/{folder}/cus_id.json','cus_id.json'])
    customer_id_file='cus_id.json'

    # build the connection to the database
    engine = mysql_connect(host, user, password, database, port,schema)
    
    # get the customer id and insert it into the sql statement
    ids = get_customer_id(customer_id_file)

    sql=f"""select customerID, CustomerName
            from customers
            where customerID in {ids} ;
         """
    # # print(engine)
    # # get the customer data from database
    #     ### method 1 execute to get result
    data = get_customer_data(engine, sql)

    #     ### method 2 use pandas to_json to get result
    # data = get_customer_data_pandas(engine, sql)

    # post data to api
    request = requests.post(api_url, data=data)
    print(request.status_code)