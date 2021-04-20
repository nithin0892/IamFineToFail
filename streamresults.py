import datetime
from nested_lookup import nested_lookup
import json
import requests
import collections
url = "https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/channels"
res = requests.get(url)
data=res.json()
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%dT%H:%M:%S"))
dict1={}
dict1['timestamp']= now.strftime("%Y-%m-%dT%H:%M:%S")
dict1['totalResults']=data['totalResults']
dict1['streamUrl']=len(nested_lookup('streamingUrl', data))
#print(dict1)
with open('data.json', 'a') as outfile:
    json.dump(dict1, outfile)
    outfile.write('\n')
url_es='http://localhost:9200/esi/_doc' 
header={'Content-Type': 'application/json'}
response=requests.post(url_es, headers=header, data=json.dumps(dict1))
print(response.text)
