from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic import ListView, DetailView
from django.core import serializers
from .models import Data, DataModelForm
from login.models import Member
from django.views.decorators.csrf import csrf_exempt

def file(request):
    if request.method=='GET':
        form = DataModelForm()
        return render(request, 'upload_files/files_form.html', {'form':form})

@csrf_exempt
def file_submit(request):
    form = DataModelForm(request.POST, request.FILES)
    print("#########POST############")
    if form.is_valid():
    # if request.is_ajax():
        print("######### is_valid() ############")
        data = form.save(commit=False)
        print(data)
        user = request.session.get('data')['user']
        # {'idx': 2, 'email': 'jinju2415@naver.com', 'id': '1064590680', 'service_type': 'KAKAO'}
        data.member_idx = Member.objects.get(idx=user['idx'])
        data.save()
        print("##################", data, "##################")
    #return HttpResponse("OK")
    return render(request, 'upload_files/files_detail.html')


class DataListView(ListView):
    model=Data
    paginate_by =5
    template_name = 'upload_files/files_list.html'

    def get_context_data(self, **kwargs):
        context = super(DataListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context

class DataDetailView(DetailView):
    model = Data
    template_name = 'upload_files/files_Detail.html'