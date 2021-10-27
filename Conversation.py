from nltk.chat.util import Chat, reflections

pairs = [
    ["(Hello Bot|Hi Bot)", ["Hello, what's your name?"]],
    ['my name is (.*)', ["hi %1"]],
    ["(hi|hello|hey)", ["hey there", "hello", "sup"]],
    ["(.*) your name", ["My name is CHATBOT"]],
    ["(Are you a robot?)", ["Yes, I'm a digital assistant named Chatbot."]],
    ["bye", ["bye! will see you soon"]],
    ["how to login", ["First verfiy yourself through mobile otp or email otp"]],
    ["i love you bot", ["Awesome. That makes me feel good."]],
    ["(sorry|my bad)", ["It's okay."]]

]


def start_chat(user_input):
    chat = Chat(pairs, reflections)
    response = chat.converse(user_input)
    return response
