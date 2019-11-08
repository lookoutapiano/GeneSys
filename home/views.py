from django.shortcuts import render



def base(request):
    return render(request, 'home/base.html')

def home(request):
<<<<<<< HEAD
    return render(request, 'home/home.html', {'title':'Test'})

def about(request):
    return render(request, 'home/about.html', {'title':'About'})

=======
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html', {'title':'About'})
>>>>>>> 03d6c7011696ecd24024fa82bac10eaac7daa114
