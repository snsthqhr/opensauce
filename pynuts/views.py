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

    gptquestion1 = diagnosis + "한국 쿠팡에서 구매가능한 영양제 제품 이름 다섯개 이내로 알려줘. 설명 없이 제품만 추천해줘."
    gptq1 = Diagnosis(content=gptquestion1)
    gptquestion2 = diagnosis + "나에게 가장 필요한 영양소 3개를 진단해줘. 설명없이 영양소만 말해줘."
    gptq2 = Question(content=gptquestion2)

    gptanswer = GPTResponse(content=chatgpt.chat_gpt(gptq1.content), explanation=chatgpt.chat_gpt(gptq2.content))
    gptanswer.save()

    context = {'gptanswer': gptanswer}

    if (gptanswer.explanation.find('바이오틱') > -1):
        context['image1'] = "https://item.kakaocdn.net/do/7971d86fcd9a1d78a6a60092f2e66e428f324a0b9c48f77dbce3a43bd11ce785"
    elif (gptanswer.explanation.find('비타민') > -1):
        context['image1'] = "data:image/jpeg;base64,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"

    if (gptanswer.explanation.find('비타민') > -1):
        context['image2'] = "data:image/jpeg;base64,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"

    if (gptanswer.explanation.find('마그네슘') > -1):
        context['image3'] = "data:image/jpeg;base64,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"




    return render(request, 'pynuts/diagnosis_result.html', context)
