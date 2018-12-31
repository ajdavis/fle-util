from pymongo import MongoClient
from bson.json_util import loads, dumps
import os
import sys

schemas = loads(open("example-schemas.json", "r").read())

if not all(arg in os.environ for arg in ["AWS_REGION", "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]):
    print "Set AWS_REGION, AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY as environment variables."
    sys.exit(1)

client = MongoClient(client_side_encryption={
  "awsRegion": os.environ["AWS_REGION"],
  "awsAccessKeyId": os.environ["AWS_ACCESS_KEY_ID"],
  "awsSecretAccessKey": os.environ["AWS_SECRET_ACCESS_KEY"],
  "schemas": schemas
})

coll = client.test.crypt

coll.drop()

coll.insert_one({ "name": "Todd Davis", "ssn": "457-55-5642" })

result = coll.find_one({ "name": "Todd Davis" })

print("Inserted and got back: {}".format(dumps(result)))

print("But 'ssn' is stored as encrypted data. Use mongo shell to see.")