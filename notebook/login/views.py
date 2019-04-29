from django.shortcuts import render, redirect, reverse, HttpResponse, HttpResponseRedirect, get_object_or_404
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

# Create your views here.
def login(request) :
    obj = ''
    try :
        if request.session['user'] is not None :
            return redirect('home')
    except KeyError:
        if request.method == 'POST' :
            try:
                # login
                obj = Member.objects.get(id=request.POST.get('id'), service_type=request.POST.get('service_type'))
            except Member.DoesNotExist:
                # join
                obj = insertMember(request)
            finally:
                serializer = MemberSerializer(obj)
                request.session['user'] = serializer.data
                tmpData = { 'name': request.POST.get('name'), 'nickname': request.POST.get('nickname'), 'profile_image': request.POST.get('profile_image') }
                request.session['tmpData'] = tmpData
                # Data.objects.all().filter(member_idx=obj)
                for data in Data.objects.all().filter(member_idx=obj):
                    # print(DataSerializer(data, context={'request': request}).data)
                    pass
                # dd = type()
                # print(dd)
                # print( [ DataSerializer(_obj).data for _obj in [ Data.objects.all().filter(member_idx=obj) ] ] )
                
                # request.session['data'] = 
                return HttpResponse(reverse('home'))
        else :
            return render(request, 'login/login.html')

def insertMember(request):
    obj = Member(email=request.POST.get('email'), id=request.POST.get('id'), service_type=request.POST.get('service_type'))
    obj.save()
    # print(UserSerializer(obj))
    return obj
