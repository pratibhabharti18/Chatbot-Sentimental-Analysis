import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses
chatbot_responses = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am just a computer program, but I am functioning well. How can I assist you?']),
    (r'what is your name', ['I am a chatbot. You can call me ChatGPT.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!']),
    (r'default', ["I'm not sure I understand.", "Could you please rephrase that?"])
]

# Create a chatbot
chatbot = Chat(chatbot_responses, reflections)

# Define a function to interact with the chatbot
def chat_with_bot():
    print("Hello! I'm a simple chatbot. You can start a conversation, or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chat_with_bot()
