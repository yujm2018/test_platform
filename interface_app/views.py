from django.shortcuts import render
from django.http import HttpResponse
import requests,json
from interface_app.form import ModuleForm

def case_manage(request):
    if request.method == "GET":
        return render(request,"case_manage.html",{"type":'list'})
    else:
        return HttpResponse('404')

# 创建/调试接口
def debug(request):
    if request.method == "GET":
        form = ModuleForm(request.GET)
        return render(request,"api_debug.html",{"type":'debug',"form":form })
    else:
        return HttpResponse('404')



def api_debug(request):
    if request.method == "POST":
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        parameter = request.POST.get("req_parameter")

        payload=json.loads(parameter.replace("'","\""))

        if method == "get":
            r = requests.get(url,params=payload)
            r = r.text

        if method == "post":
            r = requests.post(url,data=payload)
            r = r.text

        return HttpResponse(r)

    else:
        return render(request, "api_debug.html", {"type": 'debug'})
