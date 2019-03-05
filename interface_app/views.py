from django.shortcuts import render
from django.http import HttpResponse
import requests,json

def case_manage(request):
    if request.method=="GET":
        return render(request,"case_manage.html",{"type":'list'})
    else:
        return HttpResponse('404')

#创建/调试接口
def debug(request):
    if request.method=="GET":
        return render(request,"api_debug.html",{"type":'debug'})
    else:
        return HttpResponse('404')

def api_debug(request):
    if request.method == "POST":
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        parameter = request.POST.get("req_parameter")
        print(url)
        print(method)
        print(parameter)
        # payload = json.loads(parameter)

        # if request.method == "get":
        #     r = requests.get(url,parameter=payload)
        #
        # if method == "post":
        #     r = requests.post(url,data=payload)
        #
        # return HttpResponse(r.text)
        return HttpResponse("hello")

    else:
        return render(request, "api_debug.html", {"type": 'debug'})
