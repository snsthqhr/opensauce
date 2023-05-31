from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Diagnosis, GPTResponse
from . import chatgpt
def home(request):
    """
    홈페이지 출력
    """
    content = "영양제 추천 서비스"
    context = {'content': content}
    return render(request, 'pynuts/homepage.html', context)
def index(request):
    """
    설문지 출력
    """
    context = {'diagnosis': ''}
    return render(request, 'pynuts/servey_page.html', context)
def diagnosis_create(request):
    """
    설문에 대한 gpt 진단(영양제 추천)
    """

    """
    answer = Diagnosis(content=request.POST.get('content'))
    answer.save()
    gptanswer = GPTResponse(content=chatgpt.chat_gpt(answer.content))
    gptanswer.save()
    context = {'gptanswer': gptanswer}
    """
    diagnosis = ""
    gptquestion1 = ""
    gptquestion2 = ""
    eating_habits = 1

    answer = request.GET.get('digestion1')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('digestion2')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('digestion3')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('digestion4')
    if (answer != "on"):
        diagnosis += answer

    answer = request.GET.get('body_condition1')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('body_condition2')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('body_condition3')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('body_condition4')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('body_condition5')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('body_condition6')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('body_condition7')
    if (answer != "on"):
        diagnosis += answer

    answer = request.GET.get('ache1')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('ache2')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('ache3')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('ache4')
    if (answer != "on"):
        diagnosis += answer

    answer = request.GET.get('born1')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('born2')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('born3')
    if (answer != "on"):
        diagnosis += answer

    answer = request.GET.get('mouth1')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('mouth2')
    if (answer != "on"):
        diagnosis += answer
    answer = request.GET.get('mouth3')
    if (answer != "on"):
        diagnosis += answer

    answer = request.GET.get('e_habit1')
    if (answer != "on"):
        eating_habits = 2
    answer = request.GET.get('e_habit2')
    if (answer != "on"):
        eating_habits = 3



    gptquestion2 = diagnosis + "나에게 가장 필요한 영양소 5개를 진단해줘. 이유도 알려줘. 영양소만 다섯 개 이내로."
    gptq2 = Question(content=gptquestion2)
    gptanswer = GPTResponse(content=' ', explanation=chatgpt.chat_gpt(gptq2.content))
    gptanswer.save()


    """
    gptquestion1 = diagnosis + "한국 쿠팡에서 구매가능한 영양제 제품 이름 다섯개 이내로 알려줘. 설명 없이 제품만 추천해줘."
    gptq1 = Diagnosis(content=gptquestion1)
    gptq1.save()
    """

    context = {'gptanswer': gptanswer}
    return render(request, 'pynuts/diagnosis_result.html', context)
