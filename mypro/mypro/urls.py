from django.contrib import admin
from django.urls import path
from django.http import HttpRequest,HttpResponse

def home(request):

    return HttpResponse("ok")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
]
