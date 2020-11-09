#Write a program that creates a list of tuples for all the numbers in a given limit and indicate whether
#number is Prime or Non Prime. Let’s suppose limit is 7 so list should be created in the following way -
#[(2,Prime),(3,Prime),(4,Non Prime),(5,Prime),(6,Non Prime),(7,Prime)]

lower=2
upper=int(input("ENTER LIMIT : "))
print("PRIME NUMBERS B/W",lower,"&",upper,"ARE:")
for num in range(lower,upper+1):
    if (num>1):
        for i in range(2,num):
            if(num%i==0):
                print((num,"NON - PRIME"))
                break
        else:
            print((num,"PRIME"))