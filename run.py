import requests
import json
import pandas as pd

testfile = open("test.json", "a", encoding='utf-8')

url = "https://covid19.ddc.moph.go.th/api/Cases/round-3-line-lists?page=" #url end with ?page=
print("=======================\nPagination JSON API\nOutput: .json, .csv\n=======================")
startat = int(input("Start page: "))
endat = int(input("End page(0 for all of API): "))

if(endat == 0):
    response = requests.get(url + "1") 
    lastpageurl = response.json()['links']['last']
    lastpagenum = lastpageurl.split("=")[1]
    endat = lastpagenum

#for i in range(1, int(lastpagenum)+1):
for i in range(startat, endat+1):
    re = requests.get(url + str(i))
    rawget = json.dumps(re.json()['data'], ensure_ascii=False)
    if(i == 1):
        rawget = rawget[:-1] + ","
    elif(i == endat):
        rawget = rawget[1:]
    else:
        rawget = rawget[1:-1] + ","
    testfile.write(rawget)
    print("geting page " + str(i))
df = pd.read_json('test.json')
df.to_csv('test.csv', index = None)