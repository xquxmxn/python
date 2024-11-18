
# Ein Script, um automatisierte Emails zu versenden

import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv # pip install python-dotenv

PORT=25
EMAIL_SERVER = "smtp.th-wildau.de"

current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

sender_email = os.getenv("luwa2327@th-wilau.de")
password = os.getenv("Pokemon2004%?")



def send_email(subject, receiver_email, name,due_date):
    msg= EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Wassermann, Luis", f"sender_email")) #Sender Name, Sender Email
    msg["To"] = receiver_email # Receiver Email
    msg["BCC"] = sender_email # CC Email

    msg.set_content
    (
        f"""\
        Sehr geehrte Damen und Herrem, sehr geehrte Frau {name},
        Mir geht es nicht gut und nehme für den heutigen Tag, {due_date}, einen krank-ohne-Schein Tag.

        Mit freundlichen Grüßen
        Luis Wassermann
        """
    )
try:
    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("e-Mial erfolgreich gesendet")
except Exception as e:
    print(f"Fehler beim Senden der Email: {e}")

   # Send the email


if __name__ == "__main__":
    send_email(
        subject="Krank-ohne-Schein Tag",# Email Subject
        name="Koebernik", # Name der Person
        receiver_email= "luiswassermann@web.de", # receiver_email@example.com
        due_date="18, Nov 2024" # Due date
    )
