print("Words reversed")
def words_reversed(word):
    x=word.split()
    print(f'Word is splited : {x}')
    y=x[::-1]
    print(f'Splited word is reversed : {y}')
    z=' '.join(y)
    print(f'Joined the reverse splited word : {z}')

word=input("Enter the string")
words_reversed(word)
