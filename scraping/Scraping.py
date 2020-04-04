import requests
import json


class Spider():
    start_url="https://www.data.gouv.fr/api/1/datasets/?page={}&page_size=1"

    def request(self, url):      
        return  requests.get(url)

    def parse(self, url):
        myDict={}
        for i in range (1,5):
            url=self.start_url.format(3000+i)
            resp = self.request(url)
            json_resp=resp.json()
            myDict["title"]=json_resp ["data"][0]["resources"][0]["title"]
            myDict["latest"]=json_resp["data"][0]["resources"][0]["latest"]            
            yield myDict
       

a= Spider()
g=a.parse("https://www.data.gouv.fr/api/1/datasets/?page=3000&page_size=1")
for item in g : 
    print item