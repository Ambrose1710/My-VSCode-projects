import secrets 
#generates sequences of random numbers that are secure 
# generates tokens for a password reset, temopary URLs and more

import string
 
#next we will define the alphabet, what characters we will consider, from the string module
letters = string.ascii_letters #lowercase and uppercase letters
digits = string.digits #numbers 0 to 9
special_char = string.punctuation #all special characters

alphabet = letters + digits + special_char
pwd_length = 10

while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    
    if (any(char in special_char for char in pwd) and sum(char in digits for char in pwd)>=2):
        break
    
print('passsword: ' ,pwd)
