class BrandKnowledge:

    def __init__(self):

        self.brand = {
            "name": "Raremotion Labs",

            "type": "Technology studio",

            "focus": [
                "AI assistants",
                "Automation systems",
                "AI-powered tools",
                "Software projects",
                "Websites and digital systems"
            ],

            "vision": "Build useful AI products, not just learn coding."
        }


    def about_brand(self):

        return (
            f"{self.brand['name']} is a {self.brand['type']}.\n\n"
            "We build:\n"
            + "\n".join(
                f"- {item}" 
                for item in self.brand["focus"]
            )
            + "\n\nVision:\n"
            + self.brand["vision"]
        )
