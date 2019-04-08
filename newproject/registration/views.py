from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


### decorator 쓰는 방법 // 지울 예정 ###
@login_required
def post_new(request):
    pass

class LoginView(TemplateView):
    template_name = 'registration/login.html'

class LogoutView(View):
    pass

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})