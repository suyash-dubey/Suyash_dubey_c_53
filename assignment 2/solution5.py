#Write a Python function to multiply all the numbers in a list and return the result.
def mult(list):
    x=1
    for j in list:
        x=x*j
    print(x)

    
list=[]
a=0
for i in range(0,3,1):
    a = int(input("PLEASE INPUT ELEMENT: "))
    list.insert(i,a)
print(list)

mult(list)