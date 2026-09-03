questions = [
    {
        "question": "What programming language are we learning?",
        "answers": ["python"]
    },
    {
        "question": "What does AI stand for?",
        "answers": ["artificial intelligence", "ai"]
    },
    {
        "question": "What does CPU stand for?",
        "answers": ["central processing unit"]
    },
    {
        "question": "What does HTML stand for?",
        "answers": ["hypertext markup language"]
    },
    {
        "question": "What does API stand for?",
        "answers": ["application programming interface"]
    }
]


score = 0


print("🎯 Quiz Game")
print("Let's begin!")
print()


for item in questions:

    answer = input(item["question"] + " ")

    answer = answer.lower().strip()

    if answer in item["answers"]:
        print("Correct! 🎉")
        score += 1

    else:
        print("Wrong answer.")

    print()


print("Quiz finished!")
print("Your final score is:", score, "/", len(questions))
