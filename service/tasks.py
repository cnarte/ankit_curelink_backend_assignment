
from django.dispatch import receiver
from .celery.send_mail import send_mail_to


# import string
# from django.contrib.auth.models import User
# from django.utils.crypto import get_random_string


# from celery.schedules import crontab
# # from celery.app.base import add_periodic_task as periodic_task
# # from celery.decorators import periodic_task
# from celery import shared_task

# @shared_task()
# def create_random_user_accounts(total):
#     print(total)
#     # for i in range(total):
#     #     username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
#     #     email = '{}@example.com'.format(username)
#     #     password = get_random_string(50)
#     #     User.objects.create_user(username=username, email=email, password=password)
#     return '{} random users created with success!'.format (total)




# @periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
# def some_task():
#     pass
#     # do something
 
from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from django.core.mail import send_mail
from curelink.settings import EMAIL_HOST_USER



def set_schedule(year,month,day,hour,minute,mail_sub,mail_txt,recvrs):

    sched = BackgroundScheduler()


    # The job will be executed on November 6th, 2009
    receivers = ["akchy.54@gmail.com"]
    # for rec in receivers:
            
    sched.add_job(send_mail_to, 'cron', month=month, day=day, hour=hour,minute=minute,args=[mail_sub,mail_txt, recvrs])
    sched.start()
    sched.print_jobs()
# scc = BackgroundScheduler()

# @scc.scheduled_job('cron', day_of_week='mon-fri', hour=17, minute=0)
# def send_mail_to(subject, message, receivers):
#     send_mail(subject,message,EMAIL_HOST_USER,[receivers],
#     fail_silently= False)