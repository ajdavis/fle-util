# FLE Utilities #
Utilities and examples for Field-Level Encryption.

## Running the Example ##
This repository includes a very simple example of automatic encryption and decryption in [example.py](example.py).

Note, example.py __only works on macOS__ (if even that).

1. Run `mongod`.
2. Install [mockupcryptd](https://github.com/mongodb-labs/mockupcryptd) and run:
    ```
    > mongocryptd
    Listening with domain socket /tmp/mongocryptd.sock
    URI is mongodb://%2Ftmp%2Fmongocryptd.sock
    ```
3. Create an AWS account with an IAM user with privileges to create
and use keys on KMS. Note down the AWS access key ID and secret access key.
4. Create a customer master key (CMK) in the AWS console. Note down the resulting key id.
5. Install the [AWS CLI tools](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
and run:
    ```
    > aws configure
    ```
6. Install the example dependencies a new Python virtual environment. This is important, since the example
uses a forked and modified pymongo.
    ```
    > virtualenv venv
    > . ./venv/bin/activate
    > pip install -r requirements
    ```
7. Run the included setup script
    ```
    > python setup_key_vault.py
    ```
8. Run the example. This uses an example schema and automatically encrypts an "ssn" field. AWS credentials are passed through environment variables.
    ```
    > export AWS_REGION="us-east-1"
    > export AWS_ACCESS_KEY_ID="abc"
    > export AWS_SECRET_ACCESS_KEY="def"
    > python example.py
    Inserted and got back: {"ssn": "457-55-5642", "_id": {"$oid": "5c2a6f6e871516551fb90632"}, "name": "Todd Davis"}
    But 'ssn' is stored as encrypted data. Use mongo shell to see.
    ```

Setting the environment variable `MONGOCRYPT_TRACE` shows underlying tracing in libmongocrypt.
## See also ##
- [mockupcryptd](https://github.com/mongodb-labs/mockupcryptd) - a mock mongocryptd.
- [libmongocrypt](https://github.com/kevinAlbs/libmongocrypt) - a prototype C library for FLE. Communicates with KMS, mongocryptd, and does encryption.
- [pymongocrypt](https://github.com/kevinAlbs/pymongocrypt) a hacky Python wrapper around libmongocrypt.
- (coming soon) mockupkms