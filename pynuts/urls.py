from django.urls import path

from . import views

urlpatterns = [
    path('', views.home), #홈페이지
    path('servey_page/', views.index), #글씨 눌렀을때 페이지 호출
    path('diagnosis/create/', views.diagnosis_create), #답변등록 눌렀을때 페이지 호출
]