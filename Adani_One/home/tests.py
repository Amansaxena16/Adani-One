import requests

url = "https://airport-info.p.rapidapi.com/airport"


user = input("Enter your City Code : ")

querystring = {"iata": user}

headers = {
	"X-RapidAPI-Key": "dc512e1702msh15a63aeb502abe8p140103jsn1296a692297c",
	"X-RapidAPI-Host": "airport-info.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
print(data)

# airport_name = data["name"]
# country = data["country"]


# print(airport_name)
# print(country)