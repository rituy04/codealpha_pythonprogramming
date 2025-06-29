def get_chatbot_response(user_input):
    """
    Determines the chatbot's response based on the user's input.
    """
    user_input_lower = user_input.lower() # Convert input to lowercase for case-insensitivity

    if "hello" in user_input_lower or "hi" in user_input_lower:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input_lower or "how r u" in user_input_lower:
        return "I'm just a program, but I'm doing great! Thanks for asking."
    elif "bye" in user_input_lower or "goodbye" in user_input_lower:
        return "Goodbye! Have a great day!"
    elif "name" in user_input_lower:
        return "I am a simple rule-based chatbot."
    elif "help" in user_input_lower:
        return "I can respond to greetings, ask how I am, or say goodbye."
    else:
        return "I'm not sure how to respond to that. Can you try rephrasing?"

def start_chatbot():
    """
    Starts the chatbot conversation loop.
    Simulates user input as the interactive 'input()' function is not available here.
    """
    print("--- Simple Chatbot ---")
    print("Type 'quit' to exit the conversation.")

    # Simulate user inputs as direct interactive input() is not supported
    simulated_user_messages = [
        "Hello!",
        "how are you?",
        "What is your name?",
        "Can you help me?",
        "Tell me a joke", # This will trigger the default response
        "Goodbye"
    ]

    for message in simulated_user_messages:
        print(f"\nUser: {message}")
        response = get_chatbot_response(message)
        print(f"Chatbot: {response}")

        # You can add a condition here if you want to stop the simulated conversation
        # For example, if "quit" was a simulated message
        if message.lower() == 'quit':
            break

    print("\n--- Chatbot session ended ---")

# Start the chatbot
if __name__ == "__main__":
    start_chatbot()
