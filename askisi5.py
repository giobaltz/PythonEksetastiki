import tweepy
import json
import re

list_temp=[]
ntext=[]
maxnum=[]
flist=[]

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')
auth.secure=True

api = tweepy.API(auth)
try:
    twitid=input("Give a name: \n")
    for tweet in tweepy.Cursor(api.user_timeline, id=twitid).items(10):
        data=json.dumps(tweet._json)
        data1=json.loads(data)
        text=data1['text']
        list_text=re.split(r'\W+', text)
        for i in list_text:
            maxnum.append(0)
        flist+=list_text
    for y in len(flist):
        if flist[y] in flist[y:]:
            maxnum[y]+=1
    if max(maxnum)!=0:
        print (flist.index(max(maxnum)))
    else:
        print ("No word is repeated")
except :
    print("This account does not exist")
