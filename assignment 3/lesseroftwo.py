print("Lesser of two evens")


def lesser_of_two_evens(n1, n2):
    if (n1 % 2 == 0 and n2 % 2 == 0):
        if (n1 > n2):
            print(n1)
        else:
            print(n2)
    if ((n1 % 2 == 0 and n2 % 2 != 0) or (n1 % 2 != 0 and n2 % 2 == 0) or (n1 % 2 != 0 and n2 % 2 != 0)):
        if (n1 > n2):
            print(n1)
        else:
            print(n2)


n1 = int(input("Number 1 : "))
n2 = int(input("Number 2 : "))
lesser_of_two_evens(n1, n2)