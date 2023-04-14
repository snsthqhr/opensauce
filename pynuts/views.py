from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Diagnosis, GPTResponse
from . import chatgpt

def index(request):
    """
    question 목록 출력
    """
    question_list = Question.objects.order_by('content')
    context = {'question_list': question_list}
    return render(request, 'pynuts/question_list.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pynuts/question_detail.html', context)
def diagnosis_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = Diagnosis(content=request.POST.get('content'))
    answer.save()
    gptanswer = GPTResponse(content=chatgpt.chat_gpt(answer.content))
    gptanswer.save()
    return redirect('pynuts:detail', question_id=question.id)
