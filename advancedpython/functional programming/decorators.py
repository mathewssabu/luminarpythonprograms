def dec_div(func):
    def inner(n1,n2):
        if (n1<n2):
            (n1,n2)=(n2,n1)
        return func(n1,n2)
    return inner




@dec_div
def div(num1,num2):
    return num1/num2

res=div(2,10)
print(res)