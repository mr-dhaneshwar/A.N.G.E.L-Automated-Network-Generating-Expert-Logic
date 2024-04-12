import smtplib
from email.mime.text import MIMEText

mail_list = ['ghanshyam-mahajanghanshyam65@gmail.com', 'me-prasaddhaneshwar22@gmail.com',
             'kunal-ktmahajan2001@gmail.com', 'mahesh-www.mrsananse@gmail.com',
             'rishi-rushikeshprasad1185213@gmail.com', 'sanjila-sanjilaprasad687@gmail.com']


def check_mail(e):
    for i in mail_list:
        x = i.split('-')
        if e in x:
            return x
        else:
            continue


def sendEmail(to, content):
    message = MIMEText(content)
    message['From'] = 'angel.assist.2.0@gmail.com'
    message['To'] = to
    message['Subject'] = 'Email from Dhaneshwar'

    # Create SMTP session
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()

    # Login to Gmail account
    session.login('angel.assist.2.0@gmail.com', 'yrmt ihyo adbg vxve')

    # Send email
    session.sendmail('angel.assist.2.0@gmail.com', to, message.as_string())
    session.quit()
