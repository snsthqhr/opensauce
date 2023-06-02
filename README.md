# 영양제 추천 서비스
### contributor
|신동우|여은성|장호중|
|------|---|---|
| [snsthqhr](https://github.com/snsthqhr)              |      [eunseongy](https://github.com/eunseongy)         |   [mondayy1](https://github.com/mondayy1)      |
| 🌴                                               | 🔥                                               | 📖                                               |



#### 서비스 설명
본 서비스는 본인에게 필요한 영양제가 무엇인지 알고싶은 사람들을 위한 웹사이트입니다.
설문을 통해서 사용자의 현재 상태를 알고, Chatgpt를 통해 사용자에게 필요한 영양소를 진단합니다.
또한 식습관과 연관지어 본인에게 필요한 최적의 영양소와 영양제를 추천 해 줍니다.
-----
## 설치방법
본 프로젝트를 다운받고 아래의 항목 설치
```
pip install Django
pip install openai
pip install parse
```

## 의존성
```
aiohttp==3.8.4
aiosignal==1.3.1
asgiref==3.6.0
async-timeout==4.0.2
attrs==22.2.0
certifi==2022.12.7
charset-normalizer==3.1.0
Django==3.1.3
frozenlist==1.3.3
idna==3.4
multidict==6.0.4
openai==0.27.4
parse==1.19.0
pytz==2023.3
requests==2.28.2
sqlparse==0.4.3
tqdm==4.65.0
urllib3==1.26.15
yarl==1.8.2
```

## 실행방법(Development)
```
python manage.py runserver
```

----
## License
```
Copyright (c) Django Software Foundation and individual contributors.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.

    3. Neither the name of Django nor the names of its contributors may be used
       to endorse or promote products derived from this software without
       specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
