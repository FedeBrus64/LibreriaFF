from email.message import MIMEPart
import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_email(email, asunto, contenido="", archivo=None):
    usuario = "tpilibreriafyf@gmail.com"
    clave = "crvxenxrbqsdijwj"

    mime = MIMEMultipart()

    mime['Subject'] = asunto
    mime['From'] = 'Email enviado por libreriaFyF'
    mime['To'] = email

    mime.attach(MIMEText(contenido))

    if archivo is not None:
        with open(archivo, "rb") as attachment:
            base = MIMEBase('aplicacion','octet-stream')
            base.set_payload(attachment.read())
            encoders.encode_base64(base)
            base.add_header('Content.Disposition',f"attachment; filename={archivo}")
            mime.attach(base)

    context = ssl.create_default_context()

    servidor_url = "smtp.gmail.com"
    puerto = 587

    with smtplib.SMTP(servidor_url, puerto) as servidor:
        servidor.ehlo()
        servidor.starttls(context=context)
        servidor.login(usuario, clave)
        """servidor.sendmail(usuario, email, mime.as_string())"""
        servidor.send_message(mime)
    
