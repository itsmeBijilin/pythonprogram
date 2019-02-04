def power(N,k):
    if(k==1):
        return(N)
    if(k!=1):
        return(N*power(N,k-1))
N=int(input(""))
k=int(input(""))
print("",power(N,k))
