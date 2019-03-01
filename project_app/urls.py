from django.urls import path
from project_app import views

urlpattens=[

    path('project_manage',views.project_manage),
]

app_name = 'project_app'