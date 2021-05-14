import os

from flask import Flask, request
from requests import post

app = Flask(__name__)


@app.route('/multiply-webhook', methods=['POST'])
def multiply_webhook():
    # Assumes an environment variable called OUT_WEBHOOK_URLS that is a space separated list of URLs
    for webhook_url in os.environ['OUT_WEBHOOK_URLS'].split(" "):
        if request.content_type == "application/x-www-form-urlencoded":
            print("Forwarding webhook to: " + webhook_url)
            post(webhook_url,
                 data=request.form,
                 headers={"Content-Type": "application/x-www-form-urlencoded"}
                 )

    return "Endpoints multiplied!"


if __name__ == '__main__':
    app.run('localhost', 5000)
