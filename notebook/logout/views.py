# Create your views here.
from django.shortcuts import render, redirect, reverse, HttpResponse, HttpResponseRedirect, get_object_or_404

# Create your views here.
def logout(request) :
    request.session.clear()
    return HttpResponseRedirect(reverse('home'))