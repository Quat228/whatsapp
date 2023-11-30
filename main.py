import os
import requests
from dotenv import load_dotenv
from flask import Flask, request

from functions import WhatsApp, RocketChat


load_dotenv()

app = Flask(__name__)

PHONE_ID = os.environ.get("PHONE_ID")

SYSTEM_USER_TOKEN = os.environ.get("SYSTEM_USER_TOKEN")

WEBHOOK_TOKEN = os.environ.get("WEBHOOK_TOKEN")

whatsapp = WhatsApp(phone_id=PHONE_ID, token=SYSTEM_USER_TOKEN)

rocket_chat = RocketChat('http://192.168.0.133:3000')


@app.route("/hello")
def hello_world():
    if request.method == "POST":
        print('Hello, friend')
        return 'Hello, friend'
    return "<p>Hello, World!</p>"


@app.route("/check")
def check():

    url = f'https://graph.facebook.com/v18.0/{PHONE_ID}/messages'

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SYSTEM_USER_TOKEN}",
    }

    body = {

        "messaging_product": "whatsapp",
        "to": "996557132204",
        "text": {"body": "Hello my friend"},
    }

    response = requests.post(url, headers=headers, json=body)

    print(response.json())

    return 'OK', 200


@app.route("/send_message")
def send_message():
    url = f'https://graph.facebook.com/v18.0/{PHONE_ID}/messages'

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SYSTEM_USER_TOKEN}",
    }

    body = {

        "messaging_product": "whatsapp",
        "to": "996557132204",
        "text": {"body": "Hello my friend"},
    }

    response = requests.post(url, headers=headers, json=body)

    print(response.json())

    return 'OK', 200


@app.route("/webhook_income_whatsapp")
def webhook_income_whatsapp():

    parameters = request.args
    print(request.json())
    print(parameters)

    return 'OK', 200


@app.route('/webhook_outgoing_whatsapp')
def webhook_outgoing_whatsapp():

    body = request.json()

    print(body)

    return 'OK', 200

app.run()
