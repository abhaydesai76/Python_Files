from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Abhay")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I am doing good.",
    "That is good to hear",
    "Thank You",
    "You are welcome"
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

# response = chatbot.get_response("Good Morning")
# print(response)

while True:
    try:
        bot_input = chatbot.get_response("Good Morning")
        # bot_input = input()
        if bot_input == 'quit':
            break
        response = chatbot.get_response(bot_input)
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break