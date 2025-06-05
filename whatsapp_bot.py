import os
import requests
from flask import Flask, request
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN")

app = Flask(__name__)


def analyze_news(text: str) -> str:
    prompt = (
        "أنت خبير في تحليل الأخبار المتعلقة بسوق الذهب. "
        "قدّم خلاصة مختصرة مع توصية للمتداول."
    )
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": text},
    ]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content.strip()


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        return "Verification failed", 403

    data = request.get_json()
    if data.get("object") == "whatsapp_business_account":
        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])
                if not messages:
                    continue
                msg = messages[0]
                text = msg.get("text", {}).get("body", "")
                from_number = msg.get("from")
                phone_id = value.get("metadata", {}).get("phone_number_id")
                if text and phone_id and from_number:
                    analysis = analyze_news(text)
                    url = f"https://graph.facebook.com/v17.0/{phone_id}/messages"
                    headers = {
                        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
                        "Content-Type": "application/json",
                    }
                    payload = {
                        "messaging_product": "whatsapp",
                        "to": from_number,
                        "text": {"body": analysis},
                    }
                    requests.post(url, json=payload, headers=headers)
    return "ok", 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
