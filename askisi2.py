import urllib.request
import json
from datetime import date

day=date.today().day
month=date.today().month
year=date.today().year

num = input("Give 10 KINO numbers (1,80) and between them use space ' ' \n").split(" ")
num_list=list(map(int, num))

for x in range(1, day+1):
    if x<10:
        y="0"+str(x)
    if month<10:
        str_month="0"+str(month)
    site = urllib.request.Request("http://applications.opap.gr/DrawsRestServices/kino/drawDate/" + y + "-" + str_month + "-" + str(year) + ".json")
    read_site = urllib.request.urlopen(site).read()
    data=json.loads(read_site.decode('utf-8'))
    last = len(data['draws']['draw'])
    for a in range(last):
         print (data['draws']['draw'][a]['results'])
