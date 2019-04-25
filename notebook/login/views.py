from django.shortcuts import render, redirect, reverse, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from .serializers import MemberSerializer
from .models import Member
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

# Create your views here.
def login(request) :
    obj = ''
    try :
        if request.session['data']['user'] is not None :
            return redirect('home')
    except :
        if request.method == 'POST' :
            try:
                # login
                obj = Member.objects.get(id=request.POST.get('id'), service_type=request.POST.get('service_type'))
            except Member.DoesNotExist:
                # join
                obj = memberJoin(request)
            finally:
                serializer = MemberSerializer(obj)
                tmpdict = { 'name': request.POST.get('name'), 'nickname': request.POST.get('nickname'), 'profile_image': request.POST.get('profile_image') }
                tmpdict.update({ 'user' : serializer.data })
                # print(tmpdict)
                request.session['data'] = tmpdict
                return HttpResponse(reverse('home'))
        else :
            return render(request, 'login/login.html')

def memberJoin(request):
    obj = Member(email=request.POST.get('email'), id=request.POST.get('id'), service_type=request.POST.get('service_type'))
    obj.save()
    # print(UserSerializer(obj))
    return obj
