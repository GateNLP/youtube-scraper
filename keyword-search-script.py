#!/usr/bin/python

import sys
import json
import requests

if (len(sys.argv)!=4):
    print('You have not entered the arguments correctly')
    sys.exit()
print('Key: ', str(sys.argv[1]))
print('Keywords: ', str(sys.argv[2]))
print('Number of Results Needed: ', (sys.argv[3]))

if sys.argv[3] == 'all':
    print('Please wait! Extracting all videos.')
    key=str(sys.argv[1])
    q=str(sys.argv[2])
    url2='https://www.googleapis.com/youtube/v3/search?part=snippet&q='+q+'&type=video&key='+key+'&maxResults=50'
    response2 = requests.get(url2)
    dict2 = response2.json()
    nextPageToken2 = dict2.get("nextPageToken")
    while nextPageToken2:
        u2 = 'https://www.googleapis.com/youtube/v3/search?part=snippet&q='+q+'&type=video&key='+key+'&maxResults=50'+'&pageToken='+nextPageToken2
        r2 = requests.get(u2)
        jd2 = r2.json()
        dict2['items']=dict2['items']+jd2['items']
        nextPageToken2 = jd2.get("nextPageToken")
    print('Total results retrieved: ', len(dict2['items']))
    with open('keyword_search.json', 'w') as f:
        json.dump(dict2, f, indent=4)
    print('Results saved to keyword_search.json')
    sys.exit()

        
if sys.argv[3] != 'all' and int(sys.argv[3])%50 != 0:
    print('Please enter a multiple of 50 for the number of results needed')
    sys.exit()
    
key=str(sys.argv[1])
q=str(sys.argv[2])
url2='https://www.googleapis.com/youtube/v3/search?part=snippet&q='+q+'&type=video&key='+key+'&maxResults=50'
response2 = requests.get(url2)
dict2 = response2.json()

if int(sys.argv[3])==50:
    print('Total results retrieved: ', len(dict2['items']))
    with open('keyword_search.json', 'w') as f:
        json.dump(dict2, f, indent=4)
    print('Results saved to keyword_search.json')
    sys.exit()

nextPageToken2 = dict2.get("nextPageToken")

while len(dict2['items'])<int(sys.argv[3]):
    u2 ='https://www.googleapis.com/youtube/v3/search?part=snippet&q='+q+'&type=video&key='+key+'&maxResults=50'+'&pageToken='+nextPageToken2
    r2 = requests.get(u2)
    jd2 = r2.json()
    dict2['items']=dict2['items']+jd2['items']
    nextPageToken2 = jd2.get("nextPageToken")
    
print('Total results retrieved: ', len(dict2['items']))

with open('keyword_search.json', 'w') as f:
    json.dump(dict2, f, indent=4)

print('Results saved to keyword_search.json')