def fact():
    num=int(input("enter number"))
    facto=1
    for i in range(num,0,-1):
        facto=facto*i
    print(facto)
fact()
def fact(num):

    facto=1
    for i in range(num,0,-1):
        facto=facto*i
    print(facto)
fact(4)
def fact(num):

    facto=1
    for i in range(num,0,-1):
        facto=facto*i
    return facto
fac=fact(4)
print(fac)