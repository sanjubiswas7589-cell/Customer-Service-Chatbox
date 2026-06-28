from intents import responses
import re

print("=" * 50)
print("      CUSTOMER SERVICE CHATBOT")
print("=" * 50)
print("Hello! I am your virtual assistant.")
print("Type 'help' to see available topics.")
print("Type 'bye' to exit.\n")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

while True:
    user_input = input("You: ")

    cleaned_input = clean_text(user_input)

    if cleaned_input == "bye":
        print("Bot: Thank you for contacting us. Have a wonderful day!")
        break

    if cleaned_input == "help":
        print("""
I can answer questions about:

• Working hours
• Contact information
• Delivery
• Refund
• Return policy
• Payment methods
• Location
• Order status
• Cancellation
• Greetings
""")
        continue

    found = False

    for keywords, answer in responses.items():
        for keyword in keywords:
            if keyword in cleaned_input:
                print("Bot:", answer)
                found = True
                break
        if found:
            break

    if not found:
        print("Bot: Sorry, I couldn't understand your question.")
        print("Bot: Please type 'help' to see what I can answer.")
