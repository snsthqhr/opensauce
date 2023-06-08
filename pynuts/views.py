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
    return render(request, 'pynuts/homepage_introduction.html')
def page_necessity(request):
    """
    홈페이지-필요성 출력!
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
    gptquestion = ""
    eating_habits = [0, "off", "off", "off", "off", "off", "off"]

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

    """과일섭취질문. 예->비타민/많은거, 아니오->적은거"""
    answer = request.GET.get('eathabit1')
    if (answer != "on"):
        eating_habits[1] = "on"

    """규칙적인식사질문. 예->유산균/많은거"""
    answer = request.GET.get('eathabit2')
    if (answer != "on"):
        eating_habits[2] = "on"

    """편식질문. 예->마그네슘/많은거"""
    answer = request.GET.get('eathabit3')
    if (answer != "on"):
        eating_habits[3] = "on"

    """육류질문. 예->철분/많은거"""
    answer = request.GET.get('eathabit4')
    if (answer != "on"):
        eating_habits[4] = "on"

    """생선질문. 예->오메가3/많은거"""
    answer = request.GET.get('eathabit5')
    if (answer != "on"):
        eating_habits[5] = "on"

    """유제품질문. 예->칼슘/많은거"""
    answer = request.GET.get('eathabit6')
    if (answer != "on"):
        eating_habits[6] = "on"

    gptquestion = diagnosis + "나에게 가장 필요한 영양소 3개를 진단해줘. 설명없이 영양소만 말해줘. 만약 필요한 영양소 중에 비타민이 있으면 비타민은 한 종류만 말해줘."
    gptq = Question(content=gptquestion)

    gptanswer = GPTResponse(content='', explanation=chatgpt.chat_gpt(gptq.content))
    gptanswer.save()

    context = {'gptanswer': gptanswer}

    res = {'1': "on", '2': "on", '3': "on", '4': "on", '5': "on", '6': "on"}

    if (gptanswer.explanation.find('바이오틱') > -1 and res['1'] == "on"):
        res['1'] = "off"
        if (eating_habits[1] == "on"):
            context['image1'] = "https://img.danawa.com/prod_img/500000/359/849/img/5849359_1.jpg?_v=20200714153550"
            context['name1'] = "서울약사신협 프로바이오 생유산균"
            context['descrip1'] = "1일 1회 1포, 아침 공복"
        else:
            context['image1'] = "https://openimage.interpark.com/goods_image_big/9/1/4/3/8937649143_l.jpg"
            context['name1'] = "헬시오리진스 내추럴 프로바이오틱 유산균"
            context['descrip1'] = "1일 1회 1정, 아침 공복"
    elif (gptanswer.explanation.find('비타') > -1 and res['2'] == "on"):
        res['2'] = "off"
        if (eating_habits[2] == "on"):
            context['image1'] = "https://openimage.interpark.com/goods_image_big/0/7/7/1/9330140771_l.jpg"
            context['name1'] = "쏜리서치 종합비타민 투퍼데이"
            context['descrip1'] = "1일 1회 2정, 아침 식후"
        else:
            context['image1'] = "https://img2.tmon.kr/cdn4/deals/2022/12/19/16168134534/front_9d837_sgk4i.jpg"
            context['name1'] = "나우푸드 데일리 비츠 멀티 비타민"
            context['descrip1'] = "1일 1회 1정, 아침 식후"
    elif (gptanswer.explanation.find('마그네슘') > -1 and res['3'] == "on"):
        res['3'] = "off"
        if (eating_habits[3] == "on"):
            context['image1'] = "https://sitem.ssgcdn.com/91/49/79/item/1000394794991_i1_1100.jpg"
            context['name1'] = "쏜리서치 말레이트 마그네슘"
            context['descrip1'] = "1일 1회 1정, 자기 전"
        else:
            context['image1'] = "https://img.danawa.com/prod_img/500000/583/126/img/3126583_1.jpg?_v=20221207111917"
            context['name1'] = "GNC 마그네슘"
            context['descrip1'] = "1일 1회 1정, 자기 전"
    elif (gptanswer.explanation.find('철분') > -1 and res['4'] == "on"):
        res['4'] = "off"
        if (eating_habits[4] == "on"):
            context['image1'] = "https://contents.lotteon.com/itemimage/_v185646/LO/19/80/14/54/62/_1/98/01/45/46/3/LO1980145462_1980145463_1.jpg"
            context['name1'] = "나우푸드 철분 18mg 베지 캡슐"
            context['descrip1'] = "1일 1회 1정, 식후 공복"
        else:
            context['image1'] = "https://img.danawa.com/prod_img/500000/168/303/img/6303168_1.jpg?_v=20200618112935"
            context['name1'] = "네추럴라이즈 액티브 철분"
            context['descrip1'] = "1일 1회 1정, 식후 공복"
    elif (gptanswer.explanation.find('오메가') > -1 and res['5'] == "on"):
        res['5'] = "off"
        if (eating_habits[5] == "on"):
            context['image1'] = "https://www.ckdhc.com/upload/images/2021/07/07/fa9120b0174cf5adc187e09244b6609b7c640b8a09abf27163a662fd3c41a17f"
            context['name1'] = "프로메가 알티지 오메가3듀얼"
            context['descrip1'] = "1일 1회 1정, 저녁식사 직후"
        else:
            context['image1'] = "https://openimage.interpark.com/goods_image_big/0/7/5/9/11143170759_l.jpg"
            context['name1'] = "트리플스트렝스 오메가3 피쉬오일"
            context['descrip1'] = "1일 1회 1정, 저녁식사 직후"
    elif (gptanswer.explanation.find('칼슘') > -1 and res['6'] == "on"):
        res['6'] = "off"
        if (eating_habits[6] == "on"):
            context['image1'] = "https://thumbnail6.coupangcdn.com/thumbnails/remote/492x492ex/image/vendor_inventory/0183/4f7a9a844a0f5d152c98c2b21662134b904a048fe0dd033ebfd651fcd7f6.jpg"
            context['name1'] = "레인보우라이트 칼슘 타블렛"
            context['descrip1'] = "1일 1회 1정, 저녁식사 직후"
        else:
            context['image1'] = "https://openimage.interpark.com/goods_image_big/5/0/3/7/9439185037_l.jpg"
            context['name1'] = "솔가 칼슘600"
            context['descrip1'] = "1일 1회 1정, 저녁식사 직후"

    if (gptanswer.explanation.find('바이오틱') > -1 and res['1'] == "on"):
        res['1'] = "off"
        if (eating_habits[2] == "on"):
            context['image2'] = "https://img.danawa.com/prod_img/500000/359/849/img/5849359_1.jpg?_v=20200714153550"
            context['name2'] = "서울약사신협 프로바이오 생유산균"
            context['descrip2'] = "1일 1회 1포, 아침 공복"
        else:
            context['image2'] = "https://openimage.interpark.com/goods_image_big/9/1/4/3/8937649143_l.jpg"
            context['name2'] = "헬시오리진스 내추럴 프로바이오틱 유산균"
            context['descrip2'] = "1일 1회 1정, 아침 공복"
    elif (gptanswer.explanation.find('비타') > -1 and res['2'] == "on"):
        res['2'] = "off"
        if (eating_habits[2] == "on"):
            context['image2'] = "https://openimage.interpark.com/goods_image_big/0/7/7/1/9330140771_l.jpg"
            context['name2'] = "쏜리서치 종합비타민 투퍼데이"
            context['descrip2'] = "1일 1회 2정, 아침 식후"
        else:
            context['image2'] = "https://img2.tmon.kr/cdn4/deals/2022/12/19/16168134534/front_9d837_sgk4i.jpg"
            context['name2'] = "나우푸드 데일리 비츠 멀티 비타민"
            context['descrip2'] = "1일 1회 1정, 아침 식후"
    elif (gptanswer.explanation.find('마그네슘') > -1 and res['3'] == "on"):
        red['3'] = "off"
        if (eating_habits[3] == "on"):
            context['image2'] = "https://sitem.ssgcdn.com/91/49/79/item/1000394794991_i1_1100.jpg"
            context['name2'] = "쏜리서치 말레이트 마그네슘"
            context['descrip2'] = "1일 1회 1정, 자기 전"
        else:
            context['image2'] = "https://img.danawa.com/prod_img/500000/583/126/img/3126583_1.jpg?_v=20221207111917"
            context['name2'] = "GNC 마그네슘"
            context['descrip2'] = "1일 1회 1정, 자기 전"
    elif (gptanswer.explanation.find('철분') > -1 and res['4'] == "on"):
        res['4'] = "off"
        if (eating_habits[4] == "on"):
            context['image2'] = "https://contents.lotteon.com/itemimage/_v185646/LO/19/80/14/54/62/_1/98/01/45/46/3/LO1980145462_1980145463_1.jpg"
            context['name2'] = "나우푸드 철분 18mg 베지 캡슐"
            context['descrip2'] = "1일 1회 1정, 식후 공복"
        else:
            context['image2'] = "https://img.danawa.com/prod_img/500000/168/303/img/6303168_1.jpg?_v=20200618112935"
            context['name2'] = "네추럴라이즈 액티브 철분"
            context['descrip2'] = "1일 1회 1정, 식후 공복"
    elif (gptanswer.explanation.find('오메가') > -1 and res['5'] == "on"):
        res['5'] = "off"
        if (eating_habits[5] == "on"):
            context['image2'] = "https://www.ckdhc.com/upload/images/2021/07/07/fa9120b0174cf5adc187e09244b6609b7c640b8a09abf27163a662fd3c41a17f"
            context['name2'] = "프로메가 알티지 오메가3듀얼"
            context['descrip2'] = "1일 1회 1정, 저녁식사 직후"
        else:
            context['image2'] = "https://openimage.interpark.com/goods_image_big/0/7/5/9/11143170759_l.jpg"
            context['name2'] = "트리플스트렝스 오메가3 피쉬오일"
            context['descrip2'] = "1일 1회 1정, 저녁식사 직후"
    elif (gptanswer.explanation.find('칼슘') > -1 and res['6'] == "on"):
        res['6'] = "off"
        if (eating_habits[6] == "on"):
            context['image2'] = "https://thumbnail6.coupangcdn.com/thumbnails/remote/492x492ex/image/vendor_inventory/0183/4f7a9a844a0f5d152c98c2b21662134b904a048fe0dd033ebfd651fcd7f6.jpg"
            context['name2'] = "레인보우라이트 칼슘 타블렛"
            context['descrip2'] = "1일 1회 1정, 저녁식사 직후"
        else:
            context['image2'] = "https://openimage.interpark.com/goods_image_big/5/0/3/7/9439185037_l.jpg"
            context['name2'] = "솔가 칼슘600"
            context['descrip2'] = "1일 1회 1정, 저녁식사 직후"

    if (gptanswer.explanation.find('바이오틱') > -1 and res['1'] == "on"):
        res['1'] = "off"
        if (eating_habits[2] == "on"):
            context['image3'] = "https://img.danawa.com/prod_img/500000/359/849/img/5849359_1.jpg?_v=20200714153550"
            context['name3'] = "서울약사신협 프로바이오 생유산균"
            context['descrip3'] = "1일 1회 1포, 아침 공복"
        else:
            context['image3'] = "https://openimage.interpark.com/goods_image_big/9/1/4/3/8937649143_l.jpg"
            context['name3'] = "헬시오리진스 내추럴 프로바이오틱 유산균"
            context['descrip3'] = "1일 1회 1정, 아침 공복"
    elif (gptanswer.explanation.find('비타') > -1 and res['2'] == "on"):
        res['2'] = "off"
        if (eating_habits[2] == "on"):
            context['image3'] = "https://openimage.interpark.com/goods_image_big/0/7/7/1/9330140771_l.jpg"
            context['name3'] = "쏜리서치 종합비타민 투퍼데이"
            context['descrip3'] = "1일 1회 2정, 아침 식후"
        else:
            context['image3'] = "https://img2.tmon.kr/cdn4/deals/2022/12/19/16168134534/front_9d837_sgk4i.jpg"
            context['name3'] = "나우푸드 데일리 비츠 멀티 비타민"
            context['descrip3'] = "1일 1회 1정, 아침 식후"
    elif (gptanswer.explanation.find('마그네슘') > -1 and res['3'] == "on"):
        res['3'] = "off"
        if (eating_habits[3] == "on"):
            context['image3'] = "https://sitem.ssgcdn.com/91/49/79/item/1000394794991_i1_1100.jpg"
            context['name3'] = "쏜리서치 말레이트 마그네슘"
            context['descrip3'] = "1일 1회 1정, 자기 전"
        else:
            context['image3'] = "https://img.danawa.com/prod_img/500000/583/126/img/3126583_1.jpg?_v=20221207111917"
            context['name3'] = "GNC 마그네슘"
            context['descrip3'] = "1일 1회 1정, 자기 전"
    elif (gptanswer.explanation.find('철분') > -1 and res['4'] == "on"):
        res['4'] = "off"
        if (eating_habits[4] == "on"):
            context['image3'] = "https://contents.lotteon.com/itemimage/_v185646/LO/19/80/14/54/62/_1/98/01/45/46/3/LO1980145462_1980145463_1.jpg"
            context['name3'] = "나우푸드 철분 18mg 베지 캡슐"
            context['descrip3'] = "1일 1회 1정, 식후 공복"
        else:
            context['image3'] = "https://img.danawa.com/prod_img/500000/168/303/img/6303168_1.jpg?_v=20200618112935"
            context['name3'] = "네추럴라이즈 액티브 철분"
            context['descrip3'] = "1일 1회 1정, 식후 공복"
    elif (gptanswer.explanation.find('오메가') > -1 and res['5'] == "on"):
        res['5'] = "off"
        if (eating_habits[5] == "on"):
            context['image3'] = "https://www.ckdhc.com/upload/images/2021/07/07/fa9120b0174cf5adc187e09244b6609b7c640b8a09abf27163a662fd3c41a17f"
            context['name3'] = "프로메가 알티지 오메가3듀얼"
            context['descrip3'] = "1일 1회 1정, 저녁식사 직후"
        else:
            context['image3'] = "https://openimage.interpark.com/goods_image_big/0/7/5/9/11143170759_l.jpg"
            context['name3'] = "트리플스트렝스 오메가3 피쉬오일"
            context['descrip3'] = "1일 1회 1정, 저녁식사 직후"
    elif (gptanswer.explanation.find('칼슘') > -1 and res['6'] == "on"):
        res['6'] = "off"
        if (eating_habits[6] == "on"):
            context['image3'] = "https://thumbnail6.coupangcdn.com/thumbnails/remote/492x492ex/image/vendor_inventory/0183/4f7a9a844a0f5d152c98c2b21662134b904a048fe0dd033ebfd651fcd7f6.jpg"
            context['name3'] = "레인보우라이트 칼슘 타블렛"
            context['descrip3'] = "1일 1회 1정, 저녁식사 직후"
        else:
            context['image3'] = "https://openimage.interpark.com/goods_image_big/5/0/3/7/9439185037_l.jpg"
            context['name3'] = "솔가 칼슘600"
            context['descrip3'] = "1일 1회 1정, 저녁식사 직후"

    return render(request, 'pynuts/diagnosis_result.html', context)