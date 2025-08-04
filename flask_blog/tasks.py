from flask_mail import Message
from flask_blog import mail, celery

@celery.task
def send_async_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
