import chainlit as cl
import requests

async def fetch_message(message: str):
    # Fetch a message from an external API
    response = requests.get(f"http://127.0.0.1:8080/message/{message}")
    
    if response.status_code == 200:
        return response.json().get("message")
    else:
        return "Failed to fetch message,please try again."

@cl.on_chat_start
async def start():
    # Send a welcome message at the start of the conversation
    await cl.Message(
        content="👋 Welcome! I'm your AI assistant. How can I help you today?"
    ).send()

@cl.on_message
async def main(message: str):
    print(f"User message: {message.content}")
    # Process the user's message and respond
    
    response: str = await fetch_message(message.content)
    await cl.Message(
        content="🤖 AI is thinking..."
    ).send()
    # Send the AI's response
    print(f"AI response: {response}")
    await cl.Message(
        content="🤖 AI is ready to respond!"
    ).send()
    # Send the final response
    if response:
        await cl.Message(
            content=f"🤖 AI: {response}"
        ).send()
    else:
        await cl.Message(
            content="❌ Error: Unable to process your request."
        ).send()
if __name__ == "__main__":
    # Run the Chainlit app
    cl.run()