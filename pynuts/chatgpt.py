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
