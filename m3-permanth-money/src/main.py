import json
import os
import boto3

ec2 = boto3.client('ec2')
ssm = boto3.client('ssm')
id_list = []

def get_list():
  response = ec2.describe_instances(
    Filters=[{'Name': 'tag:env', 'Values': ['prod']},{'Name':'instance-state-name','Values':['running']}]
  )
  id_list.append(response['Reservations'][0]['Instances'][0]['InstanceId'])
  return id_list

def ec2_runcommand(id_list):
  response = ssm.send_command(
      InstanceIds = id_list,
      DocumentName = "AWS-RunShellScript",
      Parameters = {
          "commands": [
              "docker exec -i monthly_money_manager_app_1  bundle exec rake notification:cancellation_service"
          ],
          "executionTimeout": ['3600']
      },
  )

def lambda_handler(event, context):
  get_list()
  ec2_runcommand(id_list)
