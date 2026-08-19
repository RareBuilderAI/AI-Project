questions = [
    {
        "question": "What programming language are we learning?",
        "answer": "python"
    },
    {
        "question": "What does AI stand for?",
        "answer": "artificial intelligence"
    },
    {
        "question": "What does CPU stand for?",
        "answer": "central processing unit"
    }
]


score = 0

print("Welcome to Quiz Game 🎯")
print("Let's begin!")


for item in questions:
    answer = input(item["question"] + " ")

    if answer.lower().strip() == item["answer"]:
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong answer.")


print("Your final score is:", score, "/", len(questions))