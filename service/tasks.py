
# from celery import task
# from celery.utils.log import get_task_logger 
# from time import *

# from .celery.send_mail import send_mail_to


# sleeplogger = get_task_logger(__name__)@task(name='my_first_task')





# def my_first_task(duration):
#     subject= 'Celery'
#     message= 'My task done successfully'
#     receivers= ['receiver_mail@gmail.com']
#     is_task_completed= False
#     error=''    
#     try:
#         sleep(duration)
#         is_task_completed= True
#     except Exception as err:
#         error= str(err)
#         logger.error(error)    
    
#     if is_task_completed:
#         send_mail_to(subject,message,receivers)
#     else:
#         send_mail_to(subject,error,receivers)    
#         return('first_task_done')

import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


from celery import crontab
from celery import periodic_task

from celery import shared_task

@shared_task
def create_random_user_accounts(total):
    print(total)
    # for i in range(total):
    #     username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
    #     email = '{}@example.com'.format(username)
    #     password = get_random_string(50)
    #     User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format (total)


@periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
def some_task():
    # do something