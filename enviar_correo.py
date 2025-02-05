import smtplib
from email.message import EmailMessage
print("Holaaaaaaaaa")
remitente = "jgarcia77214@universidadean.edu.co"
destinatario = "jgarcia77214@universidadean.edu.co"
mensaje = "Hola mundo "
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario  
email["Subject"] = "Correo de prueba"
email.set_content(mensaje)

smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
smtp.starttls()
smtp.login(remitente, "SSTTQthgbh124*")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()
print("correo enviado")
