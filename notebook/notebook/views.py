from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.apps import apps
from login.models import Member
from ML.models import Data
from ML.serializers import DataSerializer
from django.db.models import Q
# import json, requests

'''
19.05.08
Android로 전송을 위해, OrderedDict -> Json 변형
'''
import json
from collections import OrderedDict

def homeView(request) :
    '''
    19.05.08
    Android 전용 분리
    '''
    if request.META['HTTP_USER_AGENT'] == 'ANDROID':
        print("Android 로 로그인했습니다.")
        obj = Member.objects.get(idx=request.META['HTTP_IDX'])
        queryset = Data.objects.filter(Q(member_idx=obj) | Q(publish=1)).values('idx', 'url', 'texts', 'date', 'publish')
        if len(queryset) > 0:
            ready_to_json_orderedDict = DataSerializer(queryset, many=True).data
            result_json = json.dumps(ready_to_json_orderedDict)
            return HttpResponse(result_json, content_type="application/json")
        else:
            return HttpResponse('None')

    # 웹 
    else :
        try :
            if request.session['user'] is not None :
                obj = Member.objects.get(idx=request.session['user']['idx'])
                # queryset = Data.objects.filter(member_idx=obj).values('idx', 'url', 'texts', 'date', 'publish')
                # queryset = Data.objects.filter(publish=1).values('idx', 'url', 'texts', 'date', 'publish')
                queryset = Data.objects.filter(Q(member_idx=obj) | Q(publish=1)).values('idx', 'url', 'texts', 'date', 'publish').order_by('-date')
                if len(queryset) > 0 :
                    print('login한 homeview - queryset EXIST')
                    request.session['data'] = DataSerializer(queryset, many = True).data
                    return render(request, 'home.html')
                else :
                    print('login한 homeview - queryset None')
                    return render(request, 'no_result.html')
            else :
                # 로그인 하지 않은 상태
                print('login하지 않은 homeview 1')
                # return render(request, 'no_user.html')
                return redirect(reverse('login:login'))
        except KeyError :
            print('login하지 않은 homeview 2')
            # return render(request, 'no_user.html')
            return redirect(reverse('login:login'))

#400에러
def bad_request_page(request, *args, **argv):
    response = render(request, "error_page.html", {})
    response.status_code = 400
    return response

#404에러
def page_not_found_page(request, *args, **argv):
    response = render(request, "error_page.html", {})
    response.status_code = 404
    return response

#500에러
def server_error_page(request, *args, **argv):
    response = render(request, "error_page.html", {})
    response.status_code = 500
    return response

#-- TemplateView
# class HomeView(TemplateView) :
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         print('\n##### context #####\n', context)
#         print()

#         print('\n##### session #####\n', self.request.session.keys())
#         print()

#         try :
#             if self.request.session['user'] is not None :
#                 obj = Member.objects.get(idx=self.request.session['user']['idx'])
#                 queryset = Data.objects.filter(member_idx=obj).values('idx', 'url', 'texts', 'date', 'publish')
#                 if queryset is not None :
#                     print('login한 homeview - queryset OK')
#                     self.request.session['data'] = DataSerializer(queryset, many = True).data
#                     template_name = 'result.html'
#                 else :
#                     print('login한 homeview - queryset X')
#                     # template_name = 'no_result.html'
#             else :
#                 # 로그인 하지 않은 상태
#                 print('login하지 않은 homeview 1')
#                 pass
#         except KeyError :
#             print('login하지 않은 homeview 2')
#             # template_name = 'no_user.html'

#         return context
