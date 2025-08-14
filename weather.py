import requests
import matplotlib.pyplot as plt
import seaborn as sns

api_key = "YOUR_API_KEY"
city = "Mumbai"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("City:", data['name'])
print("Temperature:", data['main']['temp'], "°C")
print("Humidity:", data['main']['humidity'], "%")
print("Weather:", data['weather'][0]['description'])

labels = ['Temperature', 'Humidity']
values = [data['main']['temp'], data['main']['humidity']]

plt.figure(figsize=(6, 4))
sns.barplot(x=labels, y=values, palette='viridis')
plt.title(f"Weather Report for {city}")
plt.ylabel("Values")
plt.show()

