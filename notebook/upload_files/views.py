from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.core import serializers
from .models import Data, DataModelForm
from login.models import Member


def file(request):
    if request.method=='GET':
        form = DataModelForm()
    else:
        form = DataModelForm(request.POST, request.FILES)
        if form.is_valid():
            #ModelForm ... commit 지연
            url = form.cleaned_data['url'] 
            user = request.session.get('data')['user']
            data = Data(url=url, member_idx=Member.objects.get(id=user['id']))
            data.save()
            return redirect(reverse('upload_files:list'))
        else :
            print("error....!")

    return render(request, 'upload_files/files_form.html', {'form': form})

class DataListView(ListView):
    model=Data
    paginate_by =5
    template_name = 'upload_files/files_list.html'

    def get_context_data(self, **kwargs):
        context = super(DataListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 15  # Display only 5 page numbers
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
