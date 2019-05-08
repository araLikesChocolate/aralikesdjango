from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from ML.models import Data
from ML.serializers import DataSerializer
from ML.views import simpleSentence, denseSentence
from login.models import Member
import datetime, time, os, json

# Create your views here.
'''
19.05.08
Android 추가
'''
@csrf_exempt
def deleteView(request) :
    '''
    19.05.08
    Android 추가
    '''
    if request.META['HTTP_USER_AGENT'] == 'ANDROID':
        obj = Data.objects.get(idx=request.POST.get('idx'))
        obj.delete()
        return HttpResponse("200")

    else:
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

def updateView(request) :
    try :
        if request.session['user'] is not None :
            data_instance = Data.objects.get(idx=request.POST.get('idx'))
            print(data_instance.publish)
                        
            if (data_instance.publish):
                data_instance.publish = False
                data_instance.save()
                print("@@@@@@@@@@@@@true -> false 끝@@@@@@@@@@@@@@")
            else:
                data_instance.publish = True
                data_instance.save()
                print("@@@@@@@@@@@@@false -> true 끝@@@@@@@@@@@@@@")
            return redirect('home')
        else :
            # 로그인 하지 않은 상태
            return redirect('home')
    except KeyError :
        return redirect('home')

def insert(request, params) :
    # member = Member.objects.get(id=params['id'], service_type=params['service_type'])
    member = Member.objects.get(idx=params['idx'])
    obj = Data(url=params['rename'], texts={ 'texts' : params['sentence'] }, date=datetime.datetime.now(), publish=1 if  params['publish'] == 'on' else 0, member_idx=member, model=params['model'])
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
            idx = request.META['HTTP_IDX']

            publish = request.META['HTTP_PUBLISH']
            print('\n#### ANDROID ID ####   ',  id)
            print('\n#### ANDROID SERVICE_TYPE ####   ', service_type)
            print('\n### ANDROID PUBLISH ####   ', publish)
        else :
            id = request.session['user']['id']
            service_type = request.session['user']['service_type']
            idx = request.session['user']['idx']
            publish = request.POST.get('publish')

        uploaded_file = request.FILES['image']
        extension = os.path.splitext(str(request.FILES['image']))[1]
        rename = id + '_' + str(time.strftime("%Y%m%d%H%M%S")) + extension
        fs = FileSystemStorage()
        fs.save(rename, uploaded_file)

    ################### SIMPLE MODEL ###################
    #                                                  #
        model = 'simple'
        sentence = simpleSentence(uploaded_file)  
    #                                                  #
    ####################################################
        
    ################### DENSE MODEL ###################
    #                                                  #
        # model = 'dense'
        # sentence = denseSentence(rename)  
    #                                                  #
    ####################################################

        params = { 
            # 'id': id, 
            # 'service_type': service_type, 
            'idx': idx,
            'publish': publish, 
            'rename': rename, 
            'sentence': sentence,
            'model' : model,
            }

        # DB 저장
        insert(request, params)
        
        '''
        19.05.07
        Android 추가
        '''
        if request.META['HTTP_USER_AGENT'] == 'ANDROID': 
            params = {
                # 'id': id,
                # 'service_type': service_type,
                "idx": idx,
                "publish": publish,
                "rename": rename,
                "sentence": sentence,
                "model": model,
            }
            print(params)
            return HttpResponse(json.dumps(params))
        else:
            # pass
            context = { 'uploaded_file': rename,
                        'sentences': sentence,
                    }
            return render(request, 'ML/upload_result.html', context)
    return render(request, 'ML/upload.html')