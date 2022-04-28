from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin/')
        else:
            messages.success(request,("there is somethink worng"))
            return redirect('http://127.0.0.1:8000/')
    else:
        return render(request, 'login_page/index.html')

"""
def index(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == 'POST':
        data = User(username=username, password=password)
        if data.is_valid:
            data.save()
    return render(request, 'login_page/index.html')

"""