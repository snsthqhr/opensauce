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
def page_introduction(request):
    """
    홈페이지-소개 출력
    """
    return render(request, 'pynuts/homepage_introduciton.html')
def page_necessity(request):
    """
    홈페이지-필요성 출력
    """
    return render(request, 'pynuts/homepage_necessity.html')
def page_problem(request):
    """
    홈페이지-문제 출력
    """
    return render(request, 'pynuts/homepage_problem.html')
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
        context['image1'] = "https://img.danawa.com/prod_img/500000/359/849/img/5849359_1.jpg?_v=20200714153550"
        context['name1'] = "서울약사신협 프로바이오 생유산균"
        context['descrip1'] = "1일 1회 1포, 아침 공복"
    elif (gptanswer.explanation.find('비타') > -1):
        context['image1'] = "https://contents.lotteon.com/itemimage/_v165116/LO/19/77/79/36/03/_1/97/77/93/60/4/LO1977793603_1977793604_1.jpg/dims/optimize/dims/resizemc/400x400"
        context['name1'] = "쏜리서치_종합비타민_투퍼데이"
        context['descrip1'] = "1일 1회 2정, 식후"
    elif (gptanswer.explanation.find('마그네슘') > -1):
        context['image1'] = "https://img.danawa.com/prod_img/500000/583/126/img/3126583_1.jpg?_v=20221207111917"
        context['name1'] = "GNC_마그네슘"
        context['descrip1'] = "1일 1회 1정, 자기 전"
    elif (gptanswer.explanation.find('철분') > -1):
        context['image1'] = "https://img.danawa.com/prod_img/500000/168/303/img/6303168_1.jpg?_v=20200618112935"
        context['name1'] = "네추럴라이즈 액티브 철분"
        context['descrip1'] = "1일 1회 1정, 공복"
    elif (gptanswer.explanation.find('오메가') > -1):
        context['image1'] = "https://openimage.interpark.com/goods_image_big/0/7/5/9/11143170759_l.jpg"
        context['name1'] = "트리플스트렝스_오메가3_피쉬오일"
        context['descrip1'] = "1일 1회 1정, 저녁식사 직후"
    elif (gptanswer.explanation.find('칼슘') > -1):
        context['image1'] = "https://openimage.interpark.com/goods_image_big/5/0/3/7/9439185037_l.jpg"
        context['name1'] = "솔가 칼슘600"
        context['descrip1'] = "1일 1회 1정, 저녁식사 직후"


    return render(request, 'pynuts/diagnosis_result.html', context)
