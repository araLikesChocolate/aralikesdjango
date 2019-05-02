from django.shortcuts import render, redirect
from ML.models import Data
from ML.serializers import DataSerializer
from login.models import Member
import datetime

# Create your views here.
def deleteView(request) :
    try :
        if request.session['user'] is not None :
            obj = Data.objects.get(idx=request.POST.get('idx'))
            # print(obj)
            obj.delete()
            return render(request, 'home.html')
        else :
            # 로그인 하지 않은 상태
            return redirect('home')
    except KeyError :
       return redirect('home')


def insertView(request, params) :
    obj = insertData(params['id'], params['service_type'], params['publish'], params['rename'], params['sentence'])
    print(request.META['HTTP_HOST'] + '/media/' +params['rename'])

    if request.META['HTTP_USER_AGENT'] == 'ANDROID': 
        return HttpResponse(DataSerializer(obj).data)
    else:
        # pass
        return render(request, 'ML/upload_result.html')


def insertData(id, service_type, publish, rename, sentence) :
    member = Member.objects.get(id=id, service_type=service_type)
    # print('\n### Member: ', member)
    # print(rename, sentence, datetime.datetime.now(), 0 if request.POST.get('publish') is None else 1)
    obj = Data(url=rename, texts={ 'texts' : sentence }, date=datetime.datetime.now(), publish=0 if publish is None else 1, member_idx=member)
    obj.save()
    return obj