from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ML.models import Data
from ML.serializers import DataSerializer
from ML.views import simpleSentence
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


def insert(request, params) :
    # member = Member.objects.get(id=params['id'], service_type=params['service_type'])
    member = Member.objects.get(idx=params['idx'])
    obj = insertData(params['id'], params['service_type'], params['publish'], params['rename'], params['sentence'])
    obj = Data(url=params['rename'], texts={ 'texts' : params['sentence'] }, date=datetime.datetime.now(), publish=1 if publish == 'on' else 0, member_idx=member)
    try : 
        obj.save()
        print('image DB 저장 완료!')
    except :
        print('image DB 저장 실패!')
        return render(request, 'upload_error.html')
    return obj

@csrf_exempt 
def upload(request):
    try:
        if request.META['HTTP_USER_AGENT'] == 'ANDROID':
            print('\n\n######### ANDROID #########\n\n')
            pass
        elif request.session['user'] is None:
            return redirect('home')
    except KeyError:
        return redirect('home')

    # context = {}
    if request.method == 'POST':
        if request.META['HTTP_USER_AGENT'] == 'ANDROID':
            # print('\n############ ANDROID META ############   ')
            # print(request.META)
            id = request.META['HTTP_ID']
            service_type = request.META['HTTP_SERVICE_TYPE']
            # idx = request.META['HTTP_IDX']

            publish = request.META['HTTP_PUBLISH']
            print('\n#### ANDROID ID ####   ',  id)
            print('\n#### ANDROID SERVICE_TYPE ####   ', service_type)
            print('\n### ANDROID PUBLISH ####   ', publish)
        else :
            # id = request.session['user']['id']
            # service_type = request.session['user']['service_type']
            idx = request.session['user']['idx']
            publish = request.POST.get('publish')

        uploaded_file = request.FILES['image']
        extension = os.path.splitext(str(request.FILES['image']))[1]
        # rename = id + '_' + str(time.strftime("%Y%m%d%H%M%S")) + extension
        rename = idx + '_' + str(time.strftime("%Y%m%d%H%M%S")) + extension
        fs = FileSystemStorage()
        fs.save(rename, uploaded_file)

    ################### SIMPLE MODEL ###################
    #                                                  #
        sentence = simpleSentence(uploaded_file)  
    #                                                  #
    ####################################################
        
    ################### DENSE MODEL ###################
    #                                                  #
            #    sentence = denseSentence(uploaded_file)  
    #                                                  #
    ####################################################

        params = { 
            # 'id': id, 
            # 'service_type': service_type, 
            'idx': idx,
            'publish': publish, 
            'rename': rename, 
            'sentence': sentence}

        # DB 저장
        insert(params)
        
    if request.META['HTTP_USER_AGENT'] == 'ANDROID': 
        return HttpResponse(DataSerializer(obj).data)
    else:
        # pass
        return render(request, 'ML/upload_result.html')