import requests

API_KEY = "d631fd06eb9c8c97650102dde24e80cb"  #https://home.openweathermap.org/api_keys
END_URL = "https://api.openweathermap.org/data/2.5/weather" #api calls - manual

location= input("Please input your location(city): ")
req_url=f"{END_URL}?appid={API_KEY}&q={location}"
res=requests.get(req_url)

if res.status_code == 200:
    data=res.json()
    weather=data["weather"][0]["description"]
    temperature=round(data["main"]["temp"] - 272.15,2)
    print(f'wheather in {location} is {weather} and the temperature is {temperature} celsius')

else:
    print("An error occured, please try again")