from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb',endpoint_url="https://dynamodb.us-east-1.amazonaws.com")


table = dynamodb.create_table(
    TableName='Ftp',
    KeySchema=[
        {
            'AttributeName': 'ftpkey',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'machine',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ftpkey',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'machine',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

print("Table status:", table.table_status)
