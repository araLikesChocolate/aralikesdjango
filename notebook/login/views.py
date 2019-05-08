from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from rest_framework import viewsets
# from rest_framework.request import Request
from .serializers import MemberSerializer
from .models import Member
from ML.models import Data
from ML.serializers import DataSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.
def login(request) :
    # context = {}
    obj = ''
    try :
        if request.session['user'] is not None :
            return redirect(reverse('home'))
    except KeyError:
        if request.method == 'POST' :
            try:
                # login
                obj = Member.objects.get(id=request.POST.get('id'), service_type=request.POST.get('service_type'))
            except Member.DoesNotExist:
                # join
                obj = insertMember(request)
            finally:
                '''
                ANDROID
                '''
                if request.META['HTTP_USER_AGENT'] == 'ANDROID':
                    print('\n\n######### ANDROID #########\n\n')
                    serializedCallbackForAndroid = {'idx': obj.idx }
                    print(serializedCallbackForAndroid)
                    return HttpResponse(serializedCallbackForAndroid.get('idx'))
                else:            
                    serializer = MemberSerializer(obj)
                    tmpData = { 'name': request.POST.get('name'), 'nickname': request.POST.get('nickname'), 'profile_image': request.POST.get('profile_image') }
                    # print(tmpData)
                    request.session['user'] = serializer.data
                    request.session['tmpData'] = tmpData
                    # context['user'] = obj
                    request.session.set_expiry(0)
                    return redirect(reverse('home'))
        else :
            return render(request, 'login/login.html')

def insertMember(request):
    obj = Member(email=request.POST.get('email'), id=request.POST.get('id'), service_type=request.POST.get('service_type'))
    obj.save()
    # print(UserSerializer(obj))
    return obj