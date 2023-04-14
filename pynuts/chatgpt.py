import openai
def chat_gpt(diagnosis):
    OPENAI_API_KEY = "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"
    openai.api_key = OPENAI_API_KEY
    model = "gpt-3.5-turbo"
    messages = []
    content = diagnosis
    messages.append({"role":"user", "content":content})
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages
    )
    answer = response['choices'][0]['message']['content']
    #print(f'ChatGPT: {answer}')
    return answer
