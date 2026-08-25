from weather_tool import WeatherTool


weather = WeatherTool()


print(
    weather.get_weather(
        "Lagos"
    )
)


print(
    weather.get_weather(
        "London"
    )
)
