import requests
from fastapi import FastAPI, Request, Response
from functions import WhatsApp, RocketChat

app = FastAPI()

PHONE_ID = '194838440370104'

SYSTEM_USER_TOKEN = 'EAAJSUgsWbFABO3QyExEv6tF505I3ZCTuGSq7AEpFOELcz9AzJsDRKd3ylA3Q1oT1nHA4IIwiBBH1s0AWPeWgZBdW' \
                    '0lcILsHzIJcZC883kAPKlh308kOTwWEzloPeimgfvUrFPT7YI5dOoLerULbrfkt0XMs3OnfpxZCZBzZBOLXGDr5ZCcAjMy' \
                    'EqabQcY55iJV9'


whatsapp = WhatsApp(phone_id=PHONE_ID, token=SYSTEM_USER_TOKEN)

rocket_chat = RocketChat('http://192.168.0.133:3000')


@app.get("/check")
async def check():

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

    return Response()


@app.get("/send_message")
async def send_message():
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

    return Response()


@app.get("/webhook_income_whatsapp")
async def webhook_income_whatsapp(request: Request):
    if request:
        parameters = request.query_params
        print(request.json())
        print(parameters)

    return Response()


@app.post('/webhook_outgoing_whatsapp')
async def webhook_outgoing_whatsapp(request: Request):

    body = await request.json()
    body_json = await request.body()

    print(body)

    return Response()
