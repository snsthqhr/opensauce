from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Diagnosis, GPTResponse
from . import chatgpt
def home(request):
    """
    홈페이지입니다
    """
    content = "영양제 추천 서비스"
    context = {'content': content}
    return render(request, 'pynuts/homepage.html', context)
def index(request):
    """
    question 목록(제목) 출력
    """
    question_list = Question.objects.order_by('content')
    context = {'question_list': question_list}
    return render(request, 'pynuts/servey_page.html', context)
def diagnosis_create(request):
    """
    답변에 대한 gpt 진단(영양제 추천)
    """
    answer = Diagnosis(content=request.POST.get('content'))
    answer.save()
    gptanswer = GPTResponse(content=chatgpt.chat_gpt(answer.content))
    gptanswer.save()
    context = {'gptanswer': gptanswer}
    return render(request, 'pynuts/diagnosis_result.html', context)
