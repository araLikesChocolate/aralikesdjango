from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.apps import apps
from login.models import Member
from ML.models import Data
from ML.serializers import DataSerializer
from django.db.models import Q
# import json, requests

def homeView(request) :
    try :
        if request.session['user'] is not None :
            obj = Member.objects.get(idx=request.session['user']['idx'])
            # queryset = Data.objects.filter(member_idx=obj).values('idx', 'url', 'texts', 'date', 'publish')
            # queryset = Data.objects.filter(publish=1).values('idx', 'url', 'texts', 'date', 'publish')
            queryset = Data.objects.filter(Q(member_idx=obj) | Q(publish=1)).values('idx', 'url', 'texts', 'date', 'publish')
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
            return render(request, 'no_user.html')
    except KeyError :
        print('login하지 않은 homeview 2')
        return render(request, 'no_user.html')
        # template_name = 'no_user.html'


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