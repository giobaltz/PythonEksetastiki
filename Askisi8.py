import random

num=random.sample(range(-30,30),30)
print (num)

for i in range(num):
    for j in range(i+1,num):
        y=-(num(i)+num(j))
            if (y in num):
                print (num(i),num(j),num(y))
                num.pop(i)
                num.pop(j)
                num.pop(num.index(y))
            else:
                break

print ("Αυτοί οι αριθμοί δεν μπορούν να βγάλουν αθροισμά 0", num)