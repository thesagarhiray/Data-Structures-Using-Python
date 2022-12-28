class Sort:
    def sort(self,x):
        for i in range(1,len(x)):
            key=x[i]
            j=i-1
            while j>=0 and key<=x[j]:
                x[j+1]=x[j]
                j-=1
            x[j+1]=key
class Main:
    def main():
        a=list()
        n=int(input("enter how many values : "))
        print("enter %d values :"%n)
        for i in range(0,n):
            a.append(int(input(f"enter {i+1}th value : ")))
        s=Sort()
        s.sort(a)
        print("sorted elementes are : ",a)
        return
Main.main()