import string
from random import randint
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.upper():
            return True
        
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
        
    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination :str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    
    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ''

    temp = randint(1, length)
    
    for _ in range(length - temp):
       
        new_password += combination[secrets.randbelow(combination_length)]

    t2 = 0
    if symbols:
            new_password += string.punctuation[secrets.randbelow(len(string.punctuation))]
            t2 += 1
    
    if uppercase:
        new_password += string.ascii_uppercase[secrets.randbelow(len(string.ascii_uppercase))]
        t2+=1

    for _ in range(temp - t2):
       
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


if __name__ == '__main__':
    for i in range(1,6):
        new_password: str  = generate_password(10, True, True)
        specs:str = print(f'U: {contains_upper(new_password)}, S:{contains_symbols(new_password)}')
        print(new_password)
