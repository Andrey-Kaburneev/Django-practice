from django.shortcuts import render
import random
# from django.http import HttpResponse
# Create your views here.


def index(request):
    temas = ['1', '2', '3', '4', '5']
    uniq = random.choice(temas)
    template_name = 'homepage/index.html'
    context = {
        'uniq': uniq
    }
    return render(request, template_name, context)
