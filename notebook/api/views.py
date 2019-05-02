from django.shortcuts import render, redirect
from ML.models import Data

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