import urllib.request
import json
from datetime import date

day=date.today().day
month=date.today().month
year=date.today().year

num = []
numtemp=[]
num_list=[]
num2=[]
while True:
    try:
        if len(num)==0:
            print("Give 10 unique KINO numbers [1,80] and between them use space ' '")
            num = input().split(" ")
        else:
            if len(num)<10:
                x=10-len(num2)
                print("Give ", x ," unique KINO numbers [1,80] and between them use space ' '")
                numtemp=input().split(" ")
                numtemp=list(map(int,numtemp))
        num+=numtemp
        del numtemp[:]
        del num_list[:]
        num_list=list(map(int,num))
        for t in range(len(num_list)):
            if num_list[t] not in num2:
                num2.append(num_list[t])
        if len(num2)>10:
            dia=len(num2)-10
            for a in range(dia):
                    del num2[-1]
        if len(num2)==10:
            counter=0
            for z in range(10):
                if int(num2[z])>=1 and int(num2[z])<=80:
                    counter+=1
                else:
                    num2[z]=0
            if counter==10:
                break
            else:
                for o in range(10-counter):
                    num2.remove(0)
        del num[:]
        num=num2
    except (ValueError, TypeError):
        print("Wrong input...Try again")
        del num[:]
        del num2[:]
        del numtemp[:]
        del num_list[:]

del num_list
num_list=num
print ("Your numbers is ", num_list)
day_win=[0]

for x in range(1, day+1):
    day_win.append(0)
    if x<10:
        d="0"+str(x)
    else:
        d=str(x)
    if month<10:
        str_month="0"+str(month)
    else:
        str_month=str(month)
    site = urllib.request.Request("http://applications.opap.gr/DrawsRestServices/kino/drawDate/" + d + "-" + str_month + "-" + str(year) + ".json")
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
                counter=day_win.pop()
                counter+=1
                day_win.append(counter)
                break


if max(day_win)==0:
    print("Your not lucky :-(")
else:
    print("Most of the successes in this month's KINO will be on the day(s) ")
    for i in range(1, day + 1):
        if max(day_win) == day_win[i]:
            print(i)
