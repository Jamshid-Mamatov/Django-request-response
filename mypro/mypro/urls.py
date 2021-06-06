from django.contrib import admin
from django.urls import path
from django.http import HttpRequest,HttpResponse

def home(request):
    response=HttpResponse()
    # response.write("<h1>hello django</h1>")
    # response.write("<p>start project</p>")


    # # print(response)
    # # print(type(response))
    # response.__setitem__('age',19)          # item set in header  
    # response.__setitem__('name','jamshid')

    # print(response.items())                 # information of headers

    # response.__delitem__("name")            # item of header del

    
    # print(response.items())

    
    a=request.GET.get("a")
    b=request.GET.get("b")
    sum=int(a)+int(b)
    response.write(f"<h1>Sum: {sum} </h1>")
    return response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
]
