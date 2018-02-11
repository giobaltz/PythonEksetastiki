import random

num=[]
num1=[]
num2=[]
num1 = random.sample(range(-30, 30), 30)
print(num1)
for i in range(len(num1)):
    for j in range(i+1, len(num1)):
        y=-(num1[i]+num1[j])
        if (y in num1) and not((num1[i] in num2) and (num1[j] in num2) and (y in num2)):
            print(num1[i], num1[j], y)
            num2.append(num1[i])
            num2.append(num1[j])
            num2.append(y)
        else:
            continue

for x in range(len(num1)):
            if num1[x] not in num2:
                num.append(num1[x])
if (len(num)!=0):
    print("Τhere is no possible combination of three numbers that give a sum of 0")
