"""
WhatsApp channel — Twilio WhatsApp API.

Students: implement send_whatsapp() using the Twilio Python SDK.
"""
from app.config import settings
from twilio.rest import Client

def send_whatsapp(to: str, body: str) -> str:
    """
    Send a WhatsApp message via Twilio.

    The 'to' number must be prefixed with 'whatsapp:+' (e.g. 'whatsapp:+919876543210').

    TODO:
      from twilio.rest import Client
      client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
      message = client.messages.create(
          body=body,
          from_=settings.twilio_whatsapp_number,
          to=f"whatsapp:{to}" if not to.startswith("whatsapp:") else to,
      )
      return message.sid
    """

    client = Client(
        settings.twilio_account_sid,
        settings.twilio_auth_token,
    )

    destination = (
        to
        if to.startswith("whatsapp:")
        else f"whatsapp:{to}"
    )

    message = client.messages.create(
        body=body,
        from_=settings.twilio_whatsapp_number,
        to=destination,
    )

    return message.sid