def partition(x,lb,ub):
    i=lb-1
    pivot=x[ub]
    for j in range(lb,ub):
        if x[j]<pivot:
            i=i+1
            x[i],x[j]=x[j],x[i]
    x[i+1],x[ub]=x[ub],x[i+1]
    return i+1

def sort(x,lb,ub):
    if lb < ub :
        j = partition(x,lb,ub)
        sort(x,lb,j-1)
        sort(x,j+1,ub)
class Main:
    def main():
        a=list()
        n=int(input("enter how many values : "))
        print("enter %d values :"%n)
        for i in range(0,n):
            a.append(int(input(f"enter {i+1}th value : ")))
        sort(a,0,n-1)
        print("sorted elementes are : ",a)
        return
Main.main()