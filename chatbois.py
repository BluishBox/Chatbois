import openai

openai.api_key = 'Your-API-key-here'

def chat(model, message):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response['choices'][0]['message']['content']

def argue(topic):
    message = topic
    for i in range(1000):
        if i % 2 == 0:
            message = chat("gpt-3.5-turbo", message)
            print("Chatbot 1: ", message)
        else:
            message = chat("gpt-3.5-turbo", message)
            print("Chatbot 2: ", message)

argue("Should humans colonize Mars?")

