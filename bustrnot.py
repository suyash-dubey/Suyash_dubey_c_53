print("Bust or not")
def blackjack(n1,n2,n3):
    sum=n1+n2+n3
    if(sum<=21):
        return sum
    else:
        if(n1==11 or n2==11 or n3==11):
            sum=sum-10
            if(sum<=21):
                return sum
            else:
                return 'Bust'
        else:
            return "Bust"


n1=int(input("Number 1 : "))
n2=int(input("Number 2 : "))
n3=int(input("Number 3 : "))
blackjack(n1,n2,n3)