from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status,response
from .models import *
from .tasks import *
# from tutorials.models import Tutorial
# from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view

import json
from rest_framework.decorators import api_view
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware

from django.core.mail import send_mail

def get_aware_datetime(date_str):
    ret = parse_datetime(date_str)
    if not is_aware(ret):
        ret = make_aware(ret)
    return ret
# Create your views here.
# class useringestion(APIView):
@api_view(['GET', 'POST'])
def ingest(request):
    if(request.method== 'POST'):
        data =  JSONParser().parse(request)
        user_name = data['user_name']
        topic = data['topic']
        user_mail = data['user_mail']
        usr = userandtopic(user_name=user_name,topic=topic,user_mail=user_mail)
        usr.save()

        # lis = userandtopic.objects.all()
        # print(lis[0].user_name)
        return JsonResponse({"response":'sucess',"data":data},status= status.HTTP_201_CREATED)

@api_view(["GET","POST"])
def schedule_content(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        topic = data['topic']
        content_text = data["content_text"]
        publish_time = get_aware_datetime(data["time"])
        cnt_time = contentandtimeperTopic(topic=topic,content_text=content_text,publish_time=publish_time)
        cnt_time.save()

        #schedule the cron job or clery job here with use of tasks file
        
        
        set_schedule(2022,5,6,14,49)
    # "CureLink", "Hi, This is a test email",


        return JsonResponse({"response":'sucess',"data":data},status= status.HTTP_201_CREATED)

