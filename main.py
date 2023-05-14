from tkinter import *
import requests

# Create a window
root = Tk()
root.title("My Chat App")

# Create a text box to display messages
messages = Text(root)
messages.pack()

# Create an input field for sending messages
message_box = Entry(root)
message_box.pack()

# Define the API endpoint for sending messages
SEND_MESSAGE_ENDPOINT = "http://localhost:8000/send_message"

# Define the function for sending a message
def send_message():
    message = message_box.get()
    response = requests.post(SEND_MESSAGE_ENDPOINT, json={"message": message})
    message_box.delete(0, END)

# Define the API endpoint for retrieving messages
GET_MESSAGES_ENDPOINT = "http://localhost:8000/get_messages"

# Define the function for retrieving messages
def get_messages():
    response = requests.get(GET_MESSAGES_ENDPOINT)
    messages_text = "\n".join(response.json())
    messages.delete(1.0, END)
    messages.insert(1.0, messages_text)

# Create a button to send messages
send_button = Button(root, text="Send", command=send_message)
send_button.pack()

# Create a button to retrieve messages
get_messages_button = Button(root, text="Get Messages", command=get_messages)
get_messages_button.pack()

# Start the GUI loop
root.mainloop()
