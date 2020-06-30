
def fibo(n,x,y):
    if n<=0:
        if n==0:
            print("  ",x)
        else:
            print("\n    ****  Invalid input!!  ****\n     Enter a positive integer...")
    if n==1:
        print("  ",x)
        print("  ",y)
    if n>2:
        i=0
        print("\n    "+str(x))
        print("    "+str(y))
        while i<=n:
            i=x+y
            x=y
            y=i
            if i<=n:
                print("    "+str(i))
n=int(input("\n  Enter the number upto which you want to get the Fibonacci series: "))
if n>=1:
    print("\n  The Fibonacci Series is: ")
x=0
y=1
fibo(n,x,y)
