#Write a function that checks whether a number is in a given range (inclusive of high and low).
def findrange(low,high,n):
    if(n<0):
        print("NUMBER NOT IN RANGE! ")
    elif( n > high):
        print("NUMBER NOT IN RANGE! ")
    else:
        print("NUMBER NOT IN RANGE!")

low=int(input("ENTER LOWEST : "))
high=int(input("ENTER HIGHEST : "))
n=int(input("ENTER THE NUMBER YOU ARE LOOKING FOR : "))
findrange(low,high,n)