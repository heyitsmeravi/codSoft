import random
import string
def password(lenPassword,comp):
    charactersDig=string.digits
    charactersSym=string.punctuation + string.digits
    charactersChar=string.ascii_letters + string.digits + string.punctuation
    password=''
    if comp=='simple' or comp=='s':
        for i in range(lenPassword):
            password+=random.choice(charactersDig)
    elif comp=="medium" or comp=='m':
        for i in range(lenPassword):
            password+=random.choice(charactersSym)
    elif comp=="hard" or comp=='h':
        for i in range(lenPassword):
            password+=random.choice(charactersChar)
    else:
        print("Enter Valid values")
    return password
lenPassword=int(input("Enter the lenght of Password required: "))
comp=input("Choose Password Complexity(s-simple,m-medium,h-hard): ")
print(password(lenPassword,comp))