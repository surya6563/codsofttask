import requests
import tkinter as tk
from tkinter import messagebox

class WeatherForecastApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.geometry("400x500")

        self.label = tk.Label(root, text="Enter City:")
        self.label.pack()

        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

    def get_weather(self):
        city = self.city_entry.get()

        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return

        api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            messagebox.showinfo("Weather Forecast", f"Weather in {city}:\nTemperature: {temperature}°C\nDescription: {description}")
        else:
            messagebox.showerror("Error", "Failed to fetch weather data.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherForecastApp(root)
    root.mainloop()
