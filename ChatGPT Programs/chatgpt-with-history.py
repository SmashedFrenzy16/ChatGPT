import openai

def main():

    openai.api_key = "ENTER YOUR API KEY HERE"

    user_name = input("Enter your name: ")

    behavior = input(f"Hi {user_name}, enter the style you want ChatGPT to behave in: ")

    user_question = input(f"{user_name}, enter a question for ChatGPT to answer: ")
    
    messages = [
            {"role": "system", "content": behavior}
        ]
    
    messages.append({"role": "user", "content": user_question})

    answer = openai.ChatCompletion.create(

        model = "gpt-3.5-turbo",

        messages = messages
    )

    message_body = answer.choices[0].message.content

    print(f"ChatGPT: {message_body}")
    
    {"role": "assistant", "content": message_body}

while True:

    main()

    repeat = input("Do you want to ask another question to ChatGPT (y/n)?")

    if repeat != "Y" or repeat != "y":

        break
