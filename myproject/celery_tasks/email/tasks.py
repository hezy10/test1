from django.core.mail import send_mail
from django.conf import settings


from celery_tasks.main import celery_app
@celery_app.task(name='send_email_task')
def send_email_task(message,to_email):
    print('*********************>')
    subject = '邮箱验证'
    message1 = message
    from_email = settings.EMAIL_FROM
    recipient_list = to_email
    send_mail(subject=subject, message=message1, from_email=from_email, recipient_list=recipient_list)
    print('------------->')

    # celery -A celery_tasks.main worker -l info