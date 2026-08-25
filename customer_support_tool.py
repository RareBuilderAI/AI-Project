class CustomerSupportTool:

    def __init__(self):

        self.responses = {

            "hello":
                "Hello 👋 How can I help you today?",

            "price":
                "Our team can provide pricing details.",

            "support":
                "Tell me your issue and I will help you.",

            "contact":
                "You can contact Raremotion Labs for assistance."
        }


    def answer(self, message):

        message = message.lower()


        for key in self.responses:

            if key in message:

                return self.responses[key]


        return (
            "I don't have that information yet. "
            "A team member can help you."
        )
