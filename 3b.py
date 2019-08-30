import string
from random import randint
str1=string.printable
for i in range(1,8):
    print(str1[randint(0,100)],end=" ")
