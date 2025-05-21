import chainlit as cl

@cl.on_chat_start
def start_chat():
    cl.user_message("Hello, how can I assist you today?")
    cl.bot_message("I am here to help you with your queries.")
    cl.markdown("Feel free to ask me anything!")

@cl.on_message
def handle_message(message):
    if message:
        cl.user_message(f"You said: {message}")
        cl.bot_message("Thank you for your message!")
    else:
        cl.bot_message("Please send a valid message.")
    cl.markdown("You can ask me anything related to our conversation.")