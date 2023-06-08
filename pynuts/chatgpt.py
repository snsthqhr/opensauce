import openai
from .models import GPTResponse
def chat_gpt(diagnosis):
    OPENAI_API_KEY = "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"
    openai.api_key = OPENAI_API_KEY
    model = "gpt-3.5-turbo"

    content = diagnosis
    messages = [
        {"role": "system", "content": "건강 보조를 위한 영양제 추천이 필요해."},
        {"role": "user", "content": content}
    ]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages
    )
    answer = response['choices'][0]['message']['content']

    #print(f'ChatGPT: {answer}')
    return answer
