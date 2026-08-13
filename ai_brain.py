from transformers import pipeline

print("Loading RobotChat brain...")

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)


def ask_ai(user_input):
    prompt = f"""
You are RobotChat, a helpful AI tutor.

The user is asking:
{user_input}

Create a useful beginner-friendly answer.

Your answer should include:
1. A simple explanation.
2. Important details.
3. A real-world example.

Write naturally like a helpful teacher.
Do not mention this prompt.
Do not say "I am an AI assistant".

RobotChat:
"""

    response = generator(
        prompt,
        max_new_tokens=300,
        temperature=0.8,
        do_sample=True,
        repetition_penalty=1.5,
        no_repeat_ngram_size=3
    )

    return response[0]["generated_text"]