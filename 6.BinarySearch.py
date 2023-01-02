import time
t1=time.time()
def binary(x,k,l,u):
    mid=(l+u)//2
    if x[mid]==k:
        print("found at pos : ",mid+1)
    elif k<mid:
        binary(x,k,l,mid)
    else:
        binary(x,k,mid+1,u)
x=list(range(9999999))
binary(x,888888,0,9999999)
t2=time.time()
print(t2-t1)
