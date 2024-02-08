from django.shortcuts import render
# from django.http import HttpResponse


def about(request):
    template_name = 'about/about.html'
    return render(request, template_name)
