x=input().split()
y=[]
for z in x:
    y.append(z[::-1])
for i in range(0,len(y)):
    if(i==len(y)-1):
        print(y[i],end=(""))
    else:
        print(y[i],end=(" "))
