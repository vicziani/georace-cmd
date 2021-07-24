import requests


def number_of_logs(userid):
    url_template = "https://api.geocaching.hu/logsbyuser?userid={}&fields=date&dir=desc&limit=1500"
    url = url_template.format(userid)
    response = requests.get(url)
    logs = response.json()
    #counter = 0
    #for log in logs:
    #    if log['date'].startswith('2019-'):
    #        counter = counter + 1
    #return counter
    return len(logs)

users = [{"name": "Magyusz", "id": 5108}, {"name": "Szabolcs", "id": 7542}, {"name": "Viczi", "id": 7420}]

for user in users:
  print(user["name"] + " " + str(number_of_logs(user["id"])))
