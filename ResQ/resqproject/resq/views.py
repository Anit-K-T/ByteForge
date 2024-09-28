from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import views
from .models import Hospital, ProductSupplier



def resq(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
def hospital_dashboard(request):
    hospitals = Hospital.objects.all()
    suppliers = ProductSupplier.objects.all()
    context = {
        'hospitals': hospitals,
        'suppliers': suppliers,
    }
    return render(request, 'your_template_name.html', context)
def index(request):
    return render(request, 'index.html')  

def dashboard(request):
    hospitals = Hospital.objects.all()
    suppliers = ProductSupplier.objects.all()
    context = {
        'hospitals': hospitals,
        'suppliers': suppliers,
    }
    return render(request, 'dashboard.html',context)


