# -*- coding: utf-8 -*-
from django import forms
from project_app.models import Project,Module

# # 若不勾选状态如何设置
# class ProjectForm(forms.Form):
#     name = forms.CharField(label='名称', max_length=100)
#     describe = forms.CharField(label="描述",widget=forms.Textarea)
#     status = forms.BooleanField(label="状态")

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe','status']
        # exclude = ['create_time']


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        exclude = ['create_time']