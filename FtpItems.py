from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb',endpoint_url="https://dynamodb.us-east-1.amazonaws.com")

table = dynamodb.Table('Ftp')

f = ["fkey1", "fkey2", "fkey3"]
m = ["m1", "m1", "m3"]

response = table.put_item(
   Item={
        'ftpkey': f[0],
        'machine': m[0],
        'info': {
            'connect string': "This is the connect string",
            'retries': decimal.Decimal(3),
            'schedule': "01:00"
        }
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))

response = table.put_item(
   Item={
        'ftpkey': f[1],
        'machine': m[1],
        'info': {
            'connect string': "This is another connect string",
            'retries': decimal.Decimal(3),
            'schedule': "02:00"
        }
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))

response = table.put_item(
   Item={
        'ftpkey': f[2],
        'machine': m[2],
        'info': {
            'connect string': "This is yet another connect string",
            'retries': decimal.Decimal(3),
            'schedule': "03:00"
        }
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))
