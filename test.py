import requests

url = 'http://localhost:9696/predict'
customer1 = {"job": "management", "duration": 400, "poutcome": "success"}
customer2 = {"job": "student", "duration": 280, "poutcome": "failure"}
customer3 ={"job": "management", "duration": 400, "poutcome": "success"}
response = requests.post(url, json=customer3).json()
print(response)