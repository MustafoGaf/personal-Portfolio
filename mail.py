import smtplib
from email.mime.text import MIMEText

def send_email(mail_to, sub ,message):
    sender = "mustafogaforovdev@gmail.com"
    password = "lekwrrraxyfoqfon"
     
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = sub
        server.sendmail(sender, mail_to, msg.as_string())
        return "sexs.com"
    except:
        return "EROR $)$"

def main():
    to = input("Получатель: ")
    sub = input("Тема: ")
    message = input("Сообщения: ")
    
    print(send_email(to,sub, message))
    
if __name__ == '__main__':
    main()