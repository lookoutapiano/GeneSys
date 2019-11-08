from django.shortcuts import render



def base(request):
    return render(request, 'home/base.html')

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html', {'title':'About'})

