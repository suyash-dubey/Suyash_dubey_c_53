#Write a Python function that checks whether a passed in string is palindrome or not


a=str(input("ENTER STRING: "))
print(a)
n=len(a)
print(n)
b=a[::-1]
print(b)
if(a==b):
    print("PALINDROME")
else:
    print("NOT PALINDROME")