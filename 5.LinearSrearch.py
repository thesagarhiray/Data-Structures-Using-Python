import time
t1=time.time()
def search(x,k):
    for i in range(len(x)):
        if x[i]==k:
            print("found at pos : ",i+1)
x=list(range(9999999))
k=8888888
search(x,k)
t2=time.time()
print(t2-t1)