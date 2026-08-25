class NewsTool:

    def __init__(self):

        self.news = [
            "AI technology keeps growing",
            "New software projects are being built",
            "Automation is changing businesses"
        ]


    def get_news(self):

        result = "📰 Latest News:\n\n"


        for index, article in enumerate(self.news, 1):

            result += f"{index}. {article}\n"


        return result
