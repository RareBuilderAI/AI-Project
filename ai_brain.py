import json
import urllib.request


class AIBrain:

    def __init__(self):
        self.model = "llama3.2:3b"
        self.url = "http://localhost:11434/api/generate"

    def think(self, message, memory=None, history=None):

        memory_text = ""

        if memory:
            try:
                if hasattr(memory, "show_memory"):
                    memory_text = str(memory.show_memory())
                else:
                    memory_text = str(memory)
            except Exception:
                memory_text = str(memory)

        history_text = ""

        if history:
            try:
                if hasattr(history, "show"):
                    history_text = str(history.show())
                else:
                    history_text = str(history)
            except Exception:
                history_text = str(history)

        prompt = (
            "You are RobotChat, an AI assistant built by Yhomi.\n"
            "Your mission is to help with AI, automation, coding, "
            "projects, and daily tasks.\n\n"
            "Use the memory and recent conversation when useful.\n\n"
            f"Memory:\n{memory_text}\n\n"
            f"Recent conversation:\n{history_text}\n\n"
            f"User: {message}\n"
            "RobotChat:"
        )

        return self._generate(prompt)

    def _generate(self, prompt):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            data = json.dumps(payload).encode("utf-8")

            request = urllib.request.Request(
                self.url,
                data=data,
                headers={
                    "Content-Type": "application/json"
                }
            )

            with urllib.request.urlopen(request) as response:
                result = json.loads(
                    response.read().decode("utf-8")
                )

            return result.get("response", "").strip()

        except Exception as error:
            return f"AI Brain error: {error}"


def ask_ai(message):
    brain = AIBrain()
    return brain.think(message)
