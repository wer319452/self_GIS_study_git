from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    if request.method == "POST":
        return render(request, "accountapp/hello_world.html",
                      context={'text':'POST METHOD!'}) #차이를 두기 위해 추가적인 데이터
    else:
        return render(request, "accountapp/hello_world.html",
                      context={'text':'GET METHOD!'})

