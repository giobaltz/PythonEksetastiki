file=input("Give the file name \n")
f=open(file, 'r')
flist=list(f.read())
if len(flist)<=30000:
    llist=[]
    for p in range(30000):
        llist.append(0)
    lloop=[]
    rloop=[]
    for p in range(flist):
        if flist[p]=="[":
            lloop.append(p)
        if flist[p]=="]":
            rlpop.append(p)
    if len(lloop)==len(rloop):
        p=0
        flag=False
        while p<=len(flist):
            if flist[p]=="<":
                p+=(-1)
                if p<0:
                    flag=True
                    break
            if flist[p]==">":
                p+=1
                if p>30000:
                    flag=True
                    break
            if flist[p]=="+":
                llist[p]+=1
                p+=1
            if flist[p]=="-":
                llist[p]+=(-1)
                p+=1
            if flist[p]==".":
                print (chr(llist[p]))
                p+=1
            if flist[p]==",":
                while True:
                    try:
                        x=[]
                        x=input("Give character \n")
                        if isinstance(x, str) and len(x)==1:
                            llist[p]=ord(x)
                            break
                    except TypeError:
                        print ("Try Again")
                        del x[:]
                p+=1
        if flag==True:
             print ("You break the limit...try again")
    else:
        print ("Error... problem with loops!")
else:
    print ("The file has more than 30000 characters-positions")
            
