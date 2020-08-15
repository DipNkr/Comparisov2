from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from py_scrap import helloWorld
from amzn_scrap import amzn_data


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    rply = helloWorld(msg)
    rply2=amzn_data(msg)

    # Create reply
    resp = MessagingResponse()
    resp.message(rply)
    resp.message(rply2)
    

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
