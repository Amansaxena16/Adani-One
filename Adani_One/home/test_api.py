import requests

url = "https://sky-scrapper.p.rapidapi.com/api/v1/checkServer"

headers = {
	"X-RapidAPI-Key": "dc512e1702msh15a63aeb502abe8p140103jsn1296a692297c",
	"X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

# print(response)

print(response.json())