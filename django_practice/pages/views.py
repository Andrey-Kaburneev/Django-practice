from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def integer_info(request):
    template_name = 'pages/integer.html'
    return render(request, template_name)


def collection_info(request):
    template_name = 'pages/collection.html'
    return render(request, template_name)


def string_info(request):
    template_name = 'pages/string.html'
    return render(request, template_name)


def boolean_info(request):
    template_name = 'pages/boolean.html'
    return render(request, template_name)


def data_structures_info(request):
    template_name = 'pages/data_structures.html'
    return render(request, template_name)


def algorithms_info(request):
    template_name = 'pages/algorithms.html'
    return render(request, template_name)


def method_info(request):
    template_name = 'pages/method.html'
    return render(request, template_name)
