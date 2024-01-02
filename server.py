import os
from datetime import datetime
from flask import Flask
from nanoid import generate
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import boto3

app = Flask(__name__)

flask_debug = os.environ.get("FLASK_DEBUG", False)
aws_region = os.environ.get("AWS_REGION", "us-west-2")

dynamo_db_client = boto3.resource('dynamodb', aws_region)

app.config.update({"DEBUG": bool(flask_debug)})
dynamodb_table_name="python_url_shortener"

def get_id():
    id = generate(size=10)
    return id

def put_url_id_in_dynamo(url_id, dynamodb_table_name, dynamo_db_client):

    url_table = dynamo_db_client.Table(dynamodb_table_name)

    response = url_table.put_item(
        Item={
            "url_id" : url_id,
            "url": "https://aws.amazon.com/ec2/graviton/"
        }
    )
    print(response)
    return response

@app.route("/")
def index():
    simple_date = datetime.now()
    return "Hello, World from PyPy 3, Gunicorn and Gevent! {}".format(simple_date.strftime("%Y-%m-%d %H:%M:%S.%f"))


@app.route("/shorten_url")
def shorten_url():
    url_id = get_id()
    return put_url_id_in_dynamo(url_id, dynamodb_table_name, dynamo_db_client)
    

@app.route("/test_aes_encrypt")
def test_aes_encrypt():
    key = get_random_bytes(32)
    data_to_encrypt = "tyljont@amazon.com"
    data = data_to_encrypt.encode('utf-8')
    cipher_encrypt = AES.new(key, AES.MODE_CFB)
    ciphered_bytes = cipher_encrypt.encrypt(data)

    iv = cipher_encrypt.iv
    # ciphered_data = ciphered_bytes

    cipher_decrypt = AES.new(key, AES.MODE_CFB, iv=iv)
    deciphered_bytes = cipher_decrypt.decrypt(ciphered_bytes)
    decrypted_data = deciphered_bytes.decode('utf-8')

    # assert data_to_encrypt == decrypted_data, 'Original data does not match the result'
    result = ("original data: " + str(data_to_encrypt) + " | encrypted data: " + str(ciphered_bytes) + " | decrypted data: " + str(decrypted_data))

    return (result)
