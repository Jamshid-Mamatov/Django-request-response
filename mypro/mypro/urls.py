from django.contrib import admin
from django.urls import path
from django.http import HttpRequest,HttpResponse

def home(request):
    response=HttpResponse()
    response.write("<h1>hello django</h1>")
    response.write("<p>start project</p>")
    return response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
]
