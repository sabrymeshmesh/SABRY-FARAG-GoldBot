# GoldBot WhatsApp Integration

This repo contains simple bots for Telegram and WhatsApp. `whatsapp_bot.py`
implements a minimal webhook for the [WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api).
Incoming messages are analysed using OpenAI GPT and a short trading
recommendation is sent back automatically.

## Running the WhatsApp bot

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set the following environment variables:

- `OPENAI_API_KEY` – your OpenAI key.
- `WHATSAPP_TOKEN` – token from your Meta app.
- `WHATSAPP_VERIFY_TOKEN` – webhook verification token.

3. Run the server:

```bash
python whatsapp_bot.py
```

Expose the `/webhook` endpoint publicly and configure it in your Meta
app dashboard.
