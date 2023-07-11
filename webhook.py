# So... the purpose of this app is to run a Hello-World-type script when a Twilio message is received?

# I believe these are the instructions I used: https://www.twilio.com/blog/serverless-twilio-webhooks-aws-lambda-function-urls

import os
from flask import Flask, request, abort
from twilio.request_validator import RequestValidator
from twilio.twiml.messaging_response import MessagingResponse
import boto3


app = Flask(__name__)
dynamo_client = boto3.resource("dynamodb")
dynamo_table = None

@app.route('/', methods=['POST'])
def reset():
    validator = RequestValidator(os.environ.get('TWILIO_AUTH_TOKEN'))
    try:
        if not validator.validate(
            request.url,
            request.form,
            request.headers.get('X-Twilio-Signature')
        ):
            print("Failed to authenticate")
            abort(400)
    except Exception as e:
        print(f"Authentication error: {str(e)}")

    message_body = request.form["Body"]
    try:
        if message_body.lower() == "lockbox":
            dynamo_table = "key-codes"
            code_id = "uptown-condo-front-lockbox"
        code = dynamo_table.get_item(Key={'code-id': code_id}).get("Item")
    except Exception as e:
        print(f"Authentication error: {str(e)}")
        abort(400)
    resp = MessagingResponse()
    resp.message(f"Your code is: {code}")
    return str(resp), 200, {'Content-Type': 'application/xml'}


