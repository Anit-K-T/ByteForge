from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def resq(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
def index(request):
    context = {
        'title': 'Index Page',
        'welcome_message': 'Welcome to my Django site!'
    }
    return render(request, 'index.html', context)
