from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Project,Module
from django.http import HttpResponseRedirect
from .forms import ProjectForm

@login_required()   #判断用户是否登录
def project_manage(request):
    username = request.session.get('user1','') #读取浏览器session
    project_all=Project.objects.all()

    return render(request, "project_manage.html",{
        "user":username,
        "projects":project_all,
        "type":"list"})

@login_required()
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            Project.objects.create(name=name,describe=describe)
            return HttpResponseRedirect('/manage/project_manage')
    else:
        form = ProjectForm()
    return render(request, 'project_manage.html', {'form': form,"type":"add"})

@login_required()
def edit_project(request,pid):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            model = Project.objects.get(id=pid)
            model.name = form.cleaned_data['name']
            model.describe = form.cleaned_data['describe']
            model.status = form.cleaned_data['status']
            model.save()
            return HttpResponseRedirect("/manage/project_manage")
    else:
        if pid:
            form = ProjectForm(instance=Project.objects.get(id=pid))
    return render(request, 'project_manage.html', {'form': form,"type":"edit"})

@login_required()
def delete_project(request,pid):
    Project.objects.get(id=pid).delete()
    return HttpResponseRedirect("/manage/project_manage")