# -*- coding: utf-8 -*-
from django import forms
from project_app.models import Module

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name']
        print("hello")