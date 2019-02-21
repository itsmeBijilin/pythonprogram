a=input().split()
b=[]
for x in a:
    b.append(x[::-1])
for i in range(0,len(b)):
    if(i==len(b)-1):
        print(b[i],end=(""))
    else:
        print(b[i],end=(" "))
