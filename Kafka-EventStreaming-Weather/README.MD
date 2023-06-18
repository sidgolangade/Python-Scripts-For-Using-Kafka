# Weather Data Kafka Producer - Event Streaming

This Python script fetches weather data using the OpenWeatherMap API and publishes it to a Kafka topic. It can be used to continuously fetch weather data for a specific city and stream it to a Kafka topic for further processing or analysis.

## Prerequisites

- Python 3.x
- `kafka-python` library
- OpenWeatherMap API key
- Kafka broker configuration

## Usage

- Running this script will fetch weather data for the specified city using the OpenWeatherMap API and publish it to the Kafka topic.
- The weather data will also be written to the 'weather_data.txt' file in JSON format.
- After successful execution, you will see the message "Done! The Weather Data has been successfully written to 'weather_data.txt' file."

## Customization

- If you want to modify the Kafka topic name, you can change the value of the `topic_name` variable in the script.
- To format the output differently or add more processing logic, you can modify the `publish_weather_data()` and `write_to_file()` functions.


