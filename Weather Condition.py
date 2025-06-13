import requests

with open("key.txt", "r") as f:
    API_KEY = f.read().strip()

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Istanbul"

res = requests.request("GET", url).json()

lat, lon = res["location"]["lat"], res["location"]["lon"]

temp = float(res["current"]["temp_c"])
feel_temp = float(res["current"]["feelslike_c"])
status = res["current"]["condition"]["text"]
is_day = int(res["current"]["is_day"])
cloud = int(res["current"]["cloud"])
windstatus = float(res["current"]["wind_mph"])

print(
    f"Temperature is: {temp}° but it feels like {feel_temp}°\nWeather is {status}\nWind speed is {windstatus}mph\nIt's {["night time", "daytime"][is_day]} and it's {["not ", ""][cloud]}cloudy.")

print("The weather is: ", end="")
if temp > 30:
    print("I am burning ️‍🔥‍🔥")
elif temp > 25:
    print("Okay I think")
elif temp <= 25:
    print("Are you home yet bruh")
