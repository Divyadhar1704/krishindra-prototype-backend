from chatbot.engine import ChatbotEngine


def main():

    chatbot = ChatbotEngine()

    print("=" * 40)
    print("🌱 Welcome to Krishindra Prototype")
    print("Type 'exit' to quit.")
    print("=" * 40)

    while True:

        user_message = input("\nYou: ")

        if user_message.lower() == "exit":
            print("\nBot: Goodbye! 👋")
            break

        response = chatbot.get_response(user_message)

        print(f"Bot: {response}")


if __name__ == "__main__":
    main()