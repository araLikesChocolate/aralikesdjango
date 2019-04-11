from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from .models import Data, DataModelForm



def file(request):
    if request.method=='GET':
        form = DataModelForm()
    else:
        print('저장한다.')
        form = DataModelForm(request.POST, request.FILES)
        if form.is_valid():
            #ModelForm ... commit 지연
            data = form.save(commit=False)
            data.save()
            return redirect(reverse('files:list'))

    return render(request, 'files/files_form.html', {'form': form})

class DataListView(ListView):
    model=Data
    paginate_by =5
    template_name = 'files/files_list.html'

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
