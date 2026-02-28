import requests




url = "http://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(url)
compltete_details = response.json()

for element in range(len(compltete_details)):
    print(compltete_details[element]["user"]["login"])