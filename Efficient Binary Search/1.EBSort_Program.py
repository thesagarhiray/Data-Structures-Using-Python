class Sort:
    def sort(self,l,n):
        flag=1
        if flag==1:
            for p in range(n):
                flag=0
                for i in range(n-1-p):
                    if l[i]>l[i+1]:
                        l[i] = l[i] ^ l[i + 1]
                        l[i + 1] = l[i + 1] ^ l[i]
                        l[i] = l[i] ^ l[i + 1]
                        flag=1
        return
class Main:
    def main():
        a=list()
        n=int(input("enter how many values : "))
        print("enter %d values :"%n)
        for i in range(0,n):
            a.append(int(input(f"enter {i+1}th value : ")))
        s=Sort()
        s.sort(a,n)
        print("sorted elementes are : ",a)
        return
Main.main()