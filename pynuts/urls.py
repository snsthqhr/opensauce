from django.urls import path

from . import views

app_name = 'pynuts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('diagnosis/create/<int:question_id>/', views.diagnosis_create, name='diagnosis_create'),
]