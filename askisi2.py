import urllib.request
import json
from datetime import date

day=date.today().day
month=date.today().month
year=date.today().year

num = input("Give 10 unique KINO numbers (1,80) and between them use space ' ' \n").split(" ")
num_list=list(map(int, num))
day_win=[]

for x in range(1, day+1):
    day_win.append(0)
    if x<10:
        y="0"+str(x)
    if month<10:
        str_month="0"+str(month)
    site = urllib.request.Request("http://applications.opap.gr/DrawsRestServices/kino/drawDate/" + y + "-" + str_month + "-" + str(year) + ".json")
    read_site = urllib.request.urlopen(site).read()
    data=json.loads(read_site.decode('utf-8'))
    last = len(data['draws']['draw'])
    for a in range(last):
        result = data['draws']['draw'][a]['results']
        o=0
        for i in range(10):
            if (num_list[i] in result):
                o+=1
            if o==4:
                day_win.append(x+1)
                break

max_win=max(day_win)
win=[]
for x in range(1, day+1):
    if max_win==day_win[x]:
        win.append(x)

print ("Most of the successes in this month's KINO will be on the day(s)", win)
