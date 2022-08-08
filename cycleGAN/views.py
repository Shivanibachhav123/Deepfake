from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
#from fpdf import FPDF
import ipdb


def login_user(request):
    # ipdb.set_trace()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            authorized = True
            return render(request, 'gan.html')
        else:
            messages.success(request, 'Invalid Username or Password')
            return render(request, 'login.html')
    if request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout_user(request):
    return render(request, 'logout.html')


def home(request):
    return render(request, 'home.html')


def gan(request):
    return render(request, 'gan.html')


def classify(request):
    return render(request, 'classify.html')