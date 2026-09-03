import random
import string

from calculator import Calculator


class RobotTools:

    def __init__(self):

        self.calculator = Calculator()

        self.secret_number = random.randint(1, 100)

        self.guessing_attempts = 0

        self.quiz_questions = [
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
            },
            {
                "question": "What does HTML stand for?",
                "answer": "hypertext markup language"
            },
            {
                "question": "What does API stand for?",
                "answer": "application programming interface"
            }
        ]

        self.quiz_score = 0
        self.quiz_question_index = 0

        self.contacts = {}

        self.habits = {}


    # -------------------------
    # Calculator
    # -------------------------

    def use_calculator(self, operation, a, b):

        if operation == "add":

            return self.calculator.add(a, b)

        elif operation == "subtract":

            return self.calculator.subtract(a, b)

        elif operation == "multiply":

            return self.calculator.multiply(a, b)

        elif operation == "divide":

            return self.calculator.divide(a, b)

        return "Invalid calculator operation."


    # -------------------------
    # Number Guessing Game
    # -------------------------

    def start_guessing_game(self):

        self.secret_number = random.randint(1, 100)

        self.guessing_attempts = 0

        return (
            "🎯 Number Guessing Game started! "
            "I'm thinking of a number between 1 and 100. "
            "Send me your guess."
        )


    def guess(self, command):

        try:

            number = int(command)

        except ValueError:

            return "Please send a number between 1 and 100."


        if number < 1 or number > 100:

            return "Please send a number between 1 and 100."


        self.guessing_attempts += 1


        if number < self.secret_number:

            return "Too low! Try again."


        if number > self.secret_number:

            return "Too high! Try again."


        attempts = self.guessing_attempts

        self.secret_number = random.randint(1, 100)

        self.guessing_attempts = 0

        return (
            f"Correct! 🎉 "
            f"You guessed it in {attempts} attempts."
        )


    # -------------------------
    # Quiz Game
    # -------------------------

    def start_quiz(self):

        self.quiz_score = 0

        self.quiz_question_index = 0

        question = self.quiz_questions[
            self.quiz_question_index
        ]

        return (
            "🧠 Quiz started!\n"
            "Question 1/5: "
            f"{question['question']}"
        )


    def answer_quiz(self, command):

        command = command.lower().strip()

        current_question = self.quiz_questions[
            self.quiz_question_index
        ]

        correct_answer = current_question["answer"]


        if command == correct_answer:

            self.quiz_score += 1

            response = "Correct! 🎉"

        else:

            response = (
                "Wrong answer. "
                f"The correct answer was: {correct_answer}"
            )


        self.quiz_question_index += 1


        if self.quiz_question_index >= len(
            self.quiz_questions
        ):

            final_score = self.quiz_score

            self.quiz_score = 0

            self.quiz_question_index = 0

            return (
                f"{response}\n"
                "🎯 Quiz finished! "
                f"Your final score is: {final_score} / 5"
            )


        next_question = self.quiz_questions[
            self.quiz_question_index
        ]

        question_number = (
            self.quiz_question_index + 1
        )

        return (
            f"{response} "
            f"Question {question_number}/5: "
            f"{next_question['question']}"
        )


    # -------------------------
    # Contact Book
    # -------------------------

    def add_contact(self, command):

        parts = command.split(",", 1)


        if len(parts) != 2:

            return (
                "📒 Please send the contact like this: "
                "name, phone"
            )


        name = parts[0].strip()

        phone = parts[1].strip()


        if not name or not phone:

            return (
                "📒 Please send the contact like this: "
                "name, phone"
            )


        self.contacts[name] = phone

        return (
            f"📒 Contact saved!\n"
            f"Name: {name}\n"
            f"Phone: {phone}"
        )


    def view_contacts(self):

        if not self.contacts:

            return "📒 No contacts saved yet."


        result = "📒 Contacts:\n\n"


        for name, phone in self.contacts.items():

            result += (
                f"• {name}: {phone}\n"
            )


        return result


    def delete_contact(self, command):

        parts = command.split(",", 1)

        name = parts[-1].strip()


        if name in self.contacts:

            del self.contacts[name]

            return (
                f"🗑️ Contact deleted: {name}"
            )


        return "📒 Contact not found."


    # -------------------------
    # Password Generator
    # -------------------------

    def generate_password(self, length=12):

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

        return f"🔐 Generated password: {password}"


    # -------------------------
    # Habit Tracker
    # -------------------------

    def handle_habit(self, command):

        command = command.lower().strip()

        parts = command.split(maxsplit=1)


        if len(parts) < 2:

            return (
                "🔥 Habit Tracker\n"
                "Use: add habit <name>"
            )


        action = parts[0]

        habit = parts[1]


        if action == "add":

            self.habits[habit] = 0

            return (
                f"🔥 Habit added: {habit}"
            )


        if action == "complete":

            if habit not in self.habits:

                return "🔥 Habit not found."


            self.habits[habit] += 1

            return (
                f"🔥 Habit completed: {habit}\n"
                f"Streak: {self.habits[habit]}"
            )


        if action == "view":

            if not self.habits:

                return "🔥 No habits saved yet."


            result = "🔥 Habits:\n\n"


            for name, streak in self.habits.items():

                result += (
                    f"• {name}: "
                    f"{streak} completions\n"
                )


            return result


        return (
            "🔥 Habit Tracker\n"
            "Use: add, complete, or view."
        )


    # -------------------------
    # Tool List
    # -------------------------

    def show_tools(self):

        return (
            "📝 To-Do List\n"
            "💰 Expense Tracker\n"
            "🧮 Calculator\n"
            "🎯 Number Guessing Game\n"
            "🧠 Quiz Game\n"
            "🔐 Password Generator\n"
            "📒 Contact Book\n"
            "🔥 Habit Tracker\n"
            "🌤️ Weather\n"
            "₿ Crypto Portfolio\n"
            "📰 News\n"
            "🏢 Raremotion Labs\n"
            "💬 Customer Support"
        )
