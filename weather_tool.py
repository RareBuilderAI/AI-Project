class WeatherTool:

    def __init__(self):

        self.locations = {
            "Lagos": "Sunny ☀️",
            "London": "Cloudy ☁️",
            "New York": "Rainy 🌧️"
        }


    def get_weather(self, city):

        if city in self.locations:

            return (
                f"🌤️ Weather in {city}: "
                f"{self.locations[city]}"
            )


        return "Weather information not found."
