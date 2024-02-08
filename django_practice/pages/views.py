from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def integer_info(request):
    template_name = 'pages/integer.html'
    return render(request, template_name)


def collection_info(request):
    return HttpResponse(
        '<h1>Здесь будет инфа о коллекциях</h1>'
    )


def string_info(request):
    return HttpResponse(
        '<h1>Здесь будет инфа о строковом типе данных</h1>'
    )


def boolean_info(request):
    return HttpResponse(
        '<h1>Здесь будет инфа о булевом типе данных</h1>'
    )


def data_structures_info(request):
    return HttpResponse(
        '<h1>Здесь будет инфа о структурах данных</h1>'
    )


def algorithms_info(request):
    return HttpResponse(
        '<h1>Здесь будет инфа о алгоритмах</h1>'
    )


def method_info(request):
    return HttpResponse(
        '<h1>Здесь будет инфа о методах решения алгоритмических задач</h1>'
    )
