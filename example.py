from pymongo import MongoClient
from bson.json_util import loads, dumps
import os

schemas = loads(open("schemas.json", "r").read())

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

inserting = { "name": "Todd Davis", "ssn": "457-55-5642" }

coll.insert_one(inserting)

result = coll.find_one({ "name": "Todd Davis" })

print("Got back: {}".format(dumps(result)))