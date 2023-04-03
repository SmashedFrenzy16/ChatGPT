import openai

def main():

    openai.api_key = "ENTER YOUR API KEY HERE"

    user_name = input("Enter your name: ")

    behavior = input(f"Hi {user_name}, enter the style you want ChatGPT to behave in: ")

    user_question = input(f"{user_name}: ")

    answer = openai.ChatCompletion.create(

        model = "gpt-3.5-turbo",

        messages = [
            {"role": "system", "content": behavior},
            {"role": "user", "content": user_question}
        ]
    )

    message_body = answer.choices[0].message.content

    print(f"ChatGPT: {message_body}")

while True:

    main()

    repeat = input("Do you want to ask another quesation to ChatGPT (y/n)?")

    if repeat == "Y" or repeat == "y":

        main()

    elif repeat == "n" or repeat == "N":

        break

    pass