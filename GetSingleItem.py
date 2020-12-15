import json
import boto3

def lambda_handler(event, context):
    # Varibles
    __TableName__ = "People"
    Primary_Column_Name = 'Sr'
    Primary_Key = 1
    columns=["Age","First", "Last"]
    
    # Objects
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(__TableName__)
    
    response = table.get_item(
            Key={
                'Sr': '1'
            }
        )
    
    return {
        'statusCode': 200,
        'body': response
    }
