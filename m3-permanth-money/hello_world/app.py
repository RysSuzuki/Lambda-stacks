import json
import boto3
import requests


def post_message(message):
    data={"source" : message}
    requests.post(IDOBATA_WEBHOOK_URL,data)


def lambda_handler(event, context):
    tmp = event['Records'][0]['Sns']['Message']
    message = tmp["detail"]["pipeline"] + "のステータスが変更されました" + "\n"
    message += tmp['detail']['action'] + " : "
    message += tmp["detail"]["state"]
    post_message(message)