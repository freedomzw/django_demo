from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    print(request.path)
    print(request.content_params)
    print(request.content_type)
    print(request.encoding)
    print(request.environ)
    return HttpResponse("Hello,world.You're at the Blog index")
