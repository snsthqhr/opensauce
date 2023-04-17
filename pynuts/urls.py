from django.urls import path

from . import views

urlpatterns = [
    path('', views.home), #홈페이지
    path('servey_page/', views.index), #Go눌렀을때 설문페이지 호출
    path('servey_page/diagnosis_result/', views.diagnosis_create), #제출하기 눌렀을때 진단페이지 호출
]