from transformers import pipeline


class AIBrain:

    def __init__(self):
        self.generator = pipeline(
            "text-generation",
            model="distilgpt2"
        )

    def think(self, message, memory=None, history=None):

        # Format memory
        memory_text = "No memory available."

        if memory:
            try:
                memory_data = memory.show_memory()
                if memory_data:
                    memory_text = str(memory_data)
            except Exception:
                memory_text = str(memory)

        # Format conversation history
        history_text = "No previous conversation."

        if history:
            try:
                history_data = history.show()

                if history_data:
                    history_lines = []

                    for item in history_data[-5:]:
                        user_message = item.get("user", "")
                        assistant_message = item.get("assistant", "")

                        history_lines.append(
                            f"User: {user_message}\n"
                            f"RobotChat: {assistant_message}"
                        )

                    history_text = "\n\n".join(history_lines)

            except Exception:
                history_text = str(history)

        prompt = (
            "You are RobotChat, an AI assistant built by Yhomi.\n"
            "Your mission is to help with AI, automation, coding, "
            "projects, and daily tasks.\n\n"
            f"Memory:\n{memory_text}\n\n"
            f"Recent conversation:\n{history_text}\n\n"
            f"User: {message}\n"
            "RobotChat:"
        )

        response = self.generator(
            prompt,
            max_new_tokens=100,
            temperature=0.7,
            repetition_penalty=1.5,
            no_repeat_ngram_size=3
        )

        generated = response[0]["generated_text"]

        if "RobotChat:" in generated:
            generated = generated.split("RobotChat:", 1)[1]

        return generated.strip()
