from os import listdir
from os.path import isfile, join
import requests
import json

facebook_api_key = ''
# http://stackoverflow.com/questions/12168452/long-lasting-fb-access-token-for-server-to-pull-fb-page-info Do this if token expires
payload = {'access_token': facebook_api_key}
mypath = 'generated_graphs/csv'
onlyfiles = [f.split('.')[0] for f in listdir(mypath) if isfile(join(mypath, f))]
data1 = list()
print(len(onlyfiles))
for name in onlyfiles:
    print len(data1)
    result = requests.get('https://graph.facebook.com/' + str(name), params=payload)
    try:
        data1.append({'id': name,
                      'name': result.json()['name']
                      })
    except:
        continue
with open('names.json','w') as out:
    json.dump(data1,out)