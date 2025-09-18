from transformers import pipeline
import torch

def run_chatbot():
    chatbot = pipeline("text-generation", model="gpt2")
    print("\n Simple Chatbot (type 'quit' to exit)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Chatbot: Goodbye!")
            break
        response = chatbot(user_input, max_length=50, num_return_sequences=1)
        print("Chatbot:", response[0]["generated_text"].replace(user_input, "").strip())

if __name__ == "__main__":
    run_chatbot()
