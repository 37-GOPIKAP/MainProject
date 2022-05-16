from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth import get_user_model
#User = get_user_model()
# Create your views here.

def index(request):
    return render(request,'dashboard/index.html')
    #return HttpResponse('This is the index page')

def Manager(request):
    return render(request,'manager/dashboard.html')
    #return HttpResponse('<h1 style="color:red;">This is Manager dashboard</h1>')

def Principal(request):
    return HttpResponse('This is Principal dashboard')

def AdmnStaff(request):
    return HttpResponse('This is Admninistration staff dashboard')

def Teacher(request):
    return HttpResponse('This is Teachers dashboard')

def Students(request):
    return HttpResponse('This is students dashboard')

def Parent(request):
    return HttpResponse('This is Parent dashboard')