from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    print(request.method)
    if request.method=='GET':
        return render(request, 'login.html')
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        try:
            auth.login(request, user)
        except Exception:
            messages.info(request, "Invalid Username or Password")
            return redirect('login')
        
        return render(request, 'crawler.html')