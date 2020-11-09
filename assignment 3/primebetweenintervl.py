def prime_count(n1):
    c=0
    for num in range(n1):
        if(num<=1):
            continue
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            c=c+1
    print(f'Prime numbers till {n1} => {c}')

n1=int(input("Till "))
prime_count(n1)