# So... the purpose of this app is to run a Hello-World-type script when a Twilio message is received?

# I believe these are the instructions I used: https://www.twilio.com/blog/serverless-twilio-webhooks-aws-lambda-function-urls

import os
from flask import Flask, request, abort
from twilio.request_validator import RequestValidator
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/', methods=['POST'])
def reset():
    validator = RequestValidator(os.environ.get('TWILIO_AUTH_TOKEN'))
    if not validator.validate(
            request.url,
            request.form,
            request.headers.get('X-Twilio-Signature')
    ):
        abort(400)
    message_body = request.form["Body"]
    resp = MessagingResponse()
    resp.message(f"This is literally what you just texted: {message_body}")
    return str(resp), 200, {'Content-Type': 'application/xml'}


