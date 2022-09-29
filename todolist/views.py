from http import cookies
#import imp
#from multiprocessing import context
#from operator import imod
#from turtle import title
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from todolist.models import Task
from django import forms



class TaskForm(forms.Form):
    title = forms.CharField(max_length=90)
    date = forms.DateTimeField()
    description = forms.CharField(max_length=300)

@login_required(login_url='/todolist/login')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    user = request.user
    context = {
        'list_todo': data_todolist,
        'nama': 'Tarreq',
        'user': user,
        #'last_login' : request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)

# def create_task(request):



# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            Task.objects.create(title=title, description=description, date = datetime.datetime.now(), user=request.user)
            return redirect('todolist:show_todolist')
    else:
        form = TaskForm()
    
    return render(request, 'create-task.html', {'form': form})