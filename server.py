import os
from datetime import datetime
from flask import Flask
from nanoid import generate
import boto3

app = Flask(__name__)

flask_debug = os.environ.get("FLASK_DEBUG", False)
aws_region = os.environ.get("AWS_REGION", "us-west-2")

app.config.update({"DEBUG": bool(flask_debug)})
dynamodb_table_name="python_url_shortener"

def get_id():
    id = generate(size=10)
    return id

def put_url_id_in_dynamo(url_id, dynamodb_table_name, aws_region):
    #TODO: move cliant initialization out to main function
    dynamodb = boto3.resource('dynamodb')

    url_table = dynamodb.Table(dynamodb_table_name)

    response = url_table.put_item(
        Item={
            "url_id" : url_id,
            "url": "https://aws.amazon.com/ec2/graviton/"
        }
    )
    print("stored item in dynamo")
    return response

@app.route("/")
def index():
    simple_date = datetime.now()
    return "Hello, World from PyPy 3, Gunicorn and Gevent! {}".format(simple_date.strftime("%Y-%m-%d %H:%M:%S.%f"))


@app.route("/shorten_url")
def shorten_url():
    url_id = get_id()
    return put_url_id_in_dynamo(url_id, dynamodb_table_name)
    
