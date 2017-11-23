def eval(a, b, c):
    if c == "+":
        result = a + b
    elif c == "-":
        result = a - b
    elif c == "*":
        result = a * b
    elif op == "/":
        if y == 0:
            print("sai")
        else:
            result= a / b
    return result

# a = 10
# b = 5
# c = "+"
# r = eval(x,y,c)
# print(r)

a = int(input("a = "))
b = int(input("b = "))
c = input("operation ")
if c in ["+","-","*","/"]:
    #Todo
    r = eval()

    print(r)
else:
    print("k co")
