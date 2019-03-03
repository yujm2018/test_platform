# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Module
from django.http import HttpResponseRedirect
from project_app.forms import ModuleForm

@login_required()   #判断用户是否登录
def module_manage(request):
    '''
    模块列表管理
    '''
    username = request.session.get('user1','') #读取浏览器session
    module_all=Module.objects.all()
    return render(request, "module_manage.html",{
        "user":username,
        "modules":module_all,
        "type":"list"})

@login_required()
def add_module(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project = form.cleaned_data['project']
            Module.objects.create(name=name,describe=describe,project=project)
            return HttpResponseRedirect('/manage/module_manage')
    else:
        form = ModuleForm()
    return render(request, 'module_manage.html', {'form': form,"type":"add"})

@login_required()
def edit_module(request,pid):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            model = Module.objects.get(id=pid)
            model.name = form.cleaned_data['name']
            model.describe = form.cleaned_data['describe']
            model.project = form.cleaned_data['project']
            model.save()
            return HttpResponseRedirect("/manage/module_manage")
    else:
        if pid:
            form = ModuleForm(instance=Module.objects.get(id=pid))
    return render(request, 'module_manage.html', {'form': form,"type":"edit"})

@login_required()
def delete_module(request,pid):
    Module.objects.get(id=pid).delete()
    return HttpResponseRedirect("/manage/module_manage")