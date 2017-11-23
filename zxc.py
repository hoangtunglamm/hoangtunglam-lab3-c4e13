from random import randint,choice
from test.py import eval
import test
a = randint(1,10)
b = randint(1,10)
c = choice(["+", "-", "*", "/"])
c = randint(-1,1)
d = e +c
e = eval(a, b, c)

print("{0} {3} {1} = {2}".format(a,b,d,c ))


choice = input("y or n ").lower()
if d == e:
    if choice == "y":
        print("o` dung roi` ")
    else:
        print("sai")
else:
    if choice == "y":
        print("sai")
    else:
        print("o` dung roi`")
