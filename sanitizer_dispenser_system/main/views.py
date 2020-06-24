from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


# def signup_view(request):
#     form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form':form})


def about(request):
    return render(request, 'main/about.html')


def homepage(request):
    return render(request, 'main/homepage.html')