from ..llama.llama_model import ask_llama

def chatbot():
    print("\n🤖 Hello, I am your hospital assistant robot.")
    print("I will ask you a few questions to understand your condition.\n")

    complaint = input("🧑 Please describe your problem: ")

    conversation = f"Patient complaint: {complaint}\n"

    prompt = f"""
You are a medical triage assistant.
Ask ONE relevant follow-up medical question at a time.
Cover duration, severity, medicines taken, and drug allergies.
Do not diagnose.
Conversation so far:
{conversation}
"""

    for _ in range(5):
        question = ask_llama(prompt).strip()
        print(f"\n🤖 {question}")

        answer = input("🧑 ")
        conversation += f"Q: {question}\nA: {answer}\n"

        prompt = f"""
You are a medical triage assistant.
Continue asking the next relevant medical question.
Conversation so far:
{conversation}
"""

    print("\n✅ Thank you. Your responses have been recorded.")

if __name__ == "__main__":
    chatbot()
