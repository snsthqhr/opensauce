import openai
def chat_gpt(diagnosis):
    OPENAI_API_KEY = "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"
    openai.api_key = OPENAI_API_KEY
    model = "gpt-3.5-turbo"
    content = diagnosis
    messages = [
        {"role": "system", "content": "You are a helpful assistant who recommends nutritional supplements."},
        {"role": "user", "content": content}
    ]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages
    )
    answer = response['choices'][0]['message']['content']
    #print(f'ChatGPT: {answer}')
    return answer
