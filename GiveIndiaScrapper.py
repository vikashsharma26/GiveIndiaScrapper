import requests
from bs4 import BeautifulSoup
import json
url = BeautifulSoup(requests.get("https://www.giveindia.org/certified-indian-ngos").text,"html.parser").find_all("tr",class_="jsx-697282504")[1:]
details = []
for i in url:
    data = {}
    td = i.find_all("td")
    data["Name"] = td[0].div.div.text
    data["Cause"] = td[1].text
    data["State"] = td[2].text
    details.append(data)
Data = open("Data.json","w")
json.dump(details,Data,indent=4)