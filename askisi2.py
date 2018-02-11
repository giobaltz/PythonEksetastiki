import urllib.request
import json
from datetime import date

day=date.today().day
month=date.today().month
year=date.today().year

numtemp = []
num = []
num_list = []
while True:
    try:
        x = 10 - len(num_list)
        if len(numtemp) < 10:
            print(
                "Give", x, "unique KINO numbers [1,80] and between them use space ' '")
            numtemp = input().split(" ")
        if len(numtemp) > 10:
            dia = len(numtemp) - 10
            for y in range(dia):
                del numtemp[-1]
        for t in range(len(numtemp)):
            if numtemp[t] not in num:
                num.append(numtemp[t])
        num_list = list(map(int, num))
        if len(num_list) == 10:
            counter = 0
            for z in range(10):
                if num_list[z] > 0 and num_list[z] <= 80:
                    counter += 1
                else:
                    num_list[z] = 0
            if counter == 10:
                break
            for o in range(10 - counter):
                num_list.remove(0)
        del numtemp[:]
        numtemp = num_list
    except (ValueError, TypeError):
        print("Wrong input...Try again")
        del numtemp[:]
        del num[:]
        del num_list[:]
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
