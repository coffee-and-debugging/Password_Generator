import random
import string

length=int(input("Enter the length of password: "))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbol=string.punctuation

all = lower+upper+num+symbol
temp= random.sample(all,length)

password="".join(temp)

print(password)