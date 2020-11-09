#Write  a program to print N fibonacci numbers where N is being passed from command line and you
#can run python program using command - python fibo.py 20, where N=20
print("FIBONACCI NUMBERS USING COMMAND LINE ")
import sys
def fib(n):
    a,b=0,1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n):
        fib=a+b
        a,b=b,fib
        print(fib(sys.argv[1]),end=" ")