from django.shortcuts import render
from .models import Patient

def patient(request):
    context = {
        'patients': Patient.objects.all(),
    }
    return render(request, 'patient/patient.html', context)
