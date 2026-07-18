"""
Traditional Rule-Based Chatbot
Author: JCooper
Course: Artificial Intelligence for Human-Computer Interaction

Description:
This chatbot uses predefined rules and keyword matching to respond
to common user questions. It does not use a large language model
or generative artificial intelligence.
"""

from datetime import datetime


def show_capabilities():
    """Return a list of the chatbot's supported capabilities."""

    return (
        "\nI can perform the following tasks:\n"
        "1. Respond to greetings\n"
        "2. Introduce myself\n"
        "3. Explain this project\n"
        "4. Provide course information\n"
        "5. Display today's date\n"
        "6. Display the current time\n"
        "7. Respond to simple small talk\n"
        "8. Handle blank, malformed, or unsupported input\n"
        "9. End the conversation\n"
        "\nTry typing: hello, help, about, project, course, date, time, "
        "how are you, thank you, or quit."
    )


def chatbot_response(user_input):
    """Return a predefined response based on the user's message."""

    message = user_input.lower().strip()

    # Handle blank input
    if message == "":
        return (
            "You did not enter a message. "
            "Please type a question or enter 'help' for assistance."
        )

    # Handle very short or malformed input
    if len(message) < 2:
        return (
            "That input is too short for me to understand. "
            "Please enter a complete word or question."
        )

    # Greetings
    if message in [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
    ]:
        return "Hello! Welcome to my traditional rule-based chatbot."

    # Help and capabilities
    if message in [
        "help",
        "menu",
        "capabilities",
        "what can you do",
        "show capabilities",
    ]:
        return show_capabilities()

    # About the chatbot
    if message in [
        "about",
        "who are you",
        "what are you",
        "what is your name",
        "your name",
    ]:
        return (
            "I am a traditional rule-based chatbot created in Python. "
            "I answer questions by matching user input with predefined rules."
        )

    # Project information
    if "project" in message or "assignment" in message:
        return (
            "This project demonstrates a simple traditional chatbot. "
            "The chatbot responds to multiple prompts, displays its "
            "capabilities, handles malformed input, and can be extended "
            "in the future by connecting it to an AI service."
        )

    # Course information
    if "course" in message or "class" in message:
        return (
            "This chatbot was developed for an Artificial Intelligence "
            "and Human-Computer Interaction course."
        )

    # Date
    if message in [
        "date",
        "today",
        "today's date",
        "what is the date",
        "what is today's date",
    ]:
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {current_date}."

    # Time
    if message in [
        "time",
        "current time",
        "what time is it",
        "what is the time",
    ]:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # Simple small talk
    if message in ["how are you", "how are you doing"]:
        return "I am functioning properly and ready to assist you."

    if message in ["thank you", "thanks", "thank you very much"]:
        return "You're welcome!"

    # Exit response
    if message in ["bye", "goodbye", "quit", "exit"]:
        return "Goodbye! Thank you for testing my chatbot."

    # Unsupported input
    return (
        "I am sorry, but I do not understand that question. "
        "Type 'help' to view the commands and questions I support."
    )


def run_chatbot():
    """Start and maintain the chatbot conversation."""

    print("=" * 60)
    print("              TRADITIONAL RULE-BASED CHATBOT")
    print("=" * 60)
    print("Hello! Type 'help' to see my capabilities.")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("=" * 60)

    while True:
        try:
            user_message = input("\nYou: ")
            bot_reply = chatbot_response(user_message)
            print("Bot:", bot_reply)

            if user_message.lower().strip() in [
                "bye",
                "goodbye",
                "quit",
                "exit",
            ]:
                break

        except KeyboardInterrupt:
            print("\nBot: The conversation was stopped. Goodbye!")
            break

        except Exception as error:
            print(
                "Bot: An unexpected problem occurred. "
                "Please try entering your message again."
            )
            print("Technical information:", error)


if __name__ == "__main__":
    run_chatbot()