#!/usr/bin/python

import sys
import json
import requests

if (len(sys.argv)!=3):
    print('You have not entered the arguments correctly')
    sys.exit()
print('Key: ', str(sys.argv[1]))
print('VideoID: ', str(sys.argv[2]))

key=str(sys.argv[1])
vid=str(sys.argv[2])

url='https://www.googleapis.com/youtube/v3/commentThreads?key='+key+'&textFormat=plainText&part=replies,snippet&videoId='+vid+'&maxResults=100'
response = requests.get(url)
dict = response.json()
nextPageToken = dict.get("nextPageToken")

while nextPageToken:
    u ='https://www.googleapis.com/youtube/v3/commentThreads?key='+key+'&textFormat=plainText&part=replies,snippet&videoId='+vid+'&maxResults=100'+'&pageToken='+nextPageToken
    r = requests.get(u)
    jd = r.json()
    dict['items']=dict['items']+jd['items']
    nextPageToken = jd.get("nextPageToken")
    
print("Total extracted comments: "+ str(len(dict['items'])))
print("Most recent comment: " + str(dict['items'][0]['snippet']['topLevelComment']['snippet']['textDisplay']))
print("First comment on video: " + str(dict['items'][len(dict['items'])-1]['snippet']['topLevelComment']['snippet']['textDisplay']))


with open('comments.json', 'w') as f:
    json.dump(dict, f, indent=4)

print('Results saved to comments.json')