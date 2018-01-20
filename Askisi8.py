import random

num=random.sample(range(-30, 30), 30)
print(num)
for i in range(0, len(num)):
    for j in range(i+1, len(num)):
        y=-int(num(i))-int(num(j))
        if (y in num):
            print(int(num(i)), int(num(j)), int(num(y)))
            num.pop(i)
            num.pop(j)
            num.pop(num.index(y))
        else:
            break

print("Autoi oi ariumoi den mporoun na dosoun athrisma 0", num)