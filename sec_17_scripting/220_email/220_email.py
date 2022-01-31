"""
https://docs.python.org/3/library/email.examples.html
https://docs.python.org/3/library/email.html#module-email
https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/
"""

import smtplib
from email.message import EmailMessage
from string import Template #Template genera un string que permite modificarse
from pathlib import Path

userN = "dummyhereje@gmail.com"
psw = "Tucson123"

htmlMsg = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Elhe Reje"
email["to"] = "marcosgoyret@gmail.com"
email["subject"] = "pruebas en mail"

# .substitute() devuelve un string con la substitucion hecha
# al decirle a set_content() que le cargo algo en html, se queda solo con el body
# si no le digo, envia todo el texto del archivo como se ve en VSCode
email.set_content(htmlMsg.substitute({"name": "marcos"}), "html")

"""
smtp es el protocolo de envio de mails. El numero de puerto es estandar
"""
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # hello from server
    smtp.starttls()  # tls es la encriptacion
    smtp.login(userN, psw)
    smtp.send_message(email)
    print("ALL DONE !!!!")
