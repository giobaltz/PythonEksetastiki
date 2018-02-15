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
        text1=data1['text']
        text=re.sub(r" http\S+","", text1)
        list_text=re.split(r'\W+', text)
        list_text.remove("")
        for i in list_text:
            maxnum.append(0)
        flist+=list_text
    for y in range(len(flist)):
        for j in range(y+1,len(flist)):
            if flist[y]==flist[j]:
                maxnum[y]+=1
    if max(maxnum)!=0:
        for y in range(len(maxnum)):
            if max(maxnum)==maxnum[y]:
                print (flist[maxnum.index(max(maxnum))])
    else:
        print ("No word is repeated")
except :
    print("This account does not exist")
