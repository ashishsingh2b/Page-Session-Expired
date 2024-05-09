from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def setsession(request):
    request.session ['name'] = 'Ashish'
    return render(request,'setsession.html')

def getsession(request):
    name = request.session ['name']
    return render(request,'getsession.html',{'name':name})


def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'delsession.html')