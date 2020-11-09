print("String is pangram or not \n")


def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True


str = input("Enter the string : ")
if (ispangram(str) == True):
    print("\nYes")
else:
    print("\nNo")
