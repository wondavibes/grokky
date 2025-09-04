import requests

url = "http://127.0.0.1:5000/create_user"
data = {
    "username": "jude",
    "name": "Jude",
    "age": 30,
    "title": "Mr",
    "occupation": "Engineer",
    "email": "jude144@gmail.com"
}
response = requests.post(url, json=data)
print(response.json())