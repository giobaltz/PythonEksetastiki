file=input("Give the file name \n")
f=open(file, 'r')
flist=list(f.read())

def symbols(flist, p, flag, while_loop, llist):
    if flist[p]=="\n" or flist[p]==" " or (flist[p]!="-" or flist[p]!=">" or flist[p]!="<" or flist[p]!="+" or flist[p]!="-" or flist[p]!="." or flist[p]!=", "):
        p+=1
    if llist[p]==0:
        while_loop=True
    if flist[p]=="<":
        p+=(-1)
        if p<0:
            flag=True
            while_loop=True
    if flist[p]==">":
        p+=1
        if p>30000:
            flag=True
            while_loop=True
    if flist[p]=="+":
        llist[p]+=1
        if llist[p]<0:
            llist[p]=(llist[p]-255)
        p+=1
    if flist[p]=="-":
        llist[p]+=(-1)
        if llist[p]>255:
            llist[p]=(256-llist[p])
        p+=1
    if flist[p]==".":
        print (chr(llist[p]))
        p+=1
    if flist[p]==", ":
        while True:
            x=[]
            a=input("Give character \n")
            x.append(a)
            if isinstance(x[0], str) and len(x)==1:
                llist[p]=ord(x)
                break
            else:
                print ("Try Again")
                del x[:]
                del a
        p+=1
    return(flist, p, flag, while_loop, llist);

def loop(flist, p, flag, while_loop, llist):
    while flist[p]=="]" and while_loop==False:
        symbols(flist, p, flag, while_loop,llist)
        if flist[p]=="[":
            loop(flist, p, flag)
    return(flist, p, flag, while_loop, llist);

if len(flist)<=30000:
    llist=[]
    hloop=0
    for p in range(30000):
        llist.append(0)
    flag=False
    while_loop=False
    for p in range(len(flist)):
        if flist[p]=="[" or flist[p]=="]":
            hloop+=1
    if hloop%2==0:
        p=0
        flag=False
        while p<=len(flist) and while_loop==False:
            symbols(flist, p, flag, while_loop, llist)
            if flist[p]=="[":
                loop(flist, p, flag, while_loop, llist)
        f.close()   
        if flag==True:
             print ("You break the limit...try again")
    else:
        print ("Error... problem with loops!")
else:
    print ("The file has more than 30000 characters-positions")
