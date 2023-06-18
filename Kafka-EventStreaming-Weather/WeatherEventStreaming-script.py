from kafka import KafkaProducer
import requests
import json

# Kafka broker details
bootstrap_servers = input("Enter the bootstrap_servers configuration (example: localhost:9092'): ")
topic_name = 'WeatherData'

# OpenWeatherMap API details
api_key = input("Enter your Weather API Key: ")
city = input("Enter the City Name: ")

# Kafka producer setup
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def fetch_weather_data():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Error fetching weather data: {response.status_code}')
        return None

def publish_weather_data(data):
    producer.send(topic_name, value=data)
    print(f'Published weather data to Kafka topic: {topic_name}')

def write_to_file(data):
    with open('weather_data.txt', 'w') as file:
        file.write(json.dumps(data))
        
def main():
    weather_data = fetch_weather_data()
    if weather_data:
        publish_weather_data(weather_data)
        write_to_file(weather_data)

if __name__ == '__main__':
    main()

print("Done! The Weather Data has been successfully written to 'weather_data.txt' file.")


