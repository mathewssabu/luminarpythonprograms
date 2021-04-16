#reduce
lst=[10,20,30,40,50]
from functools import reduce

total=reduce(lambda num1,num2:num1+num2,lst)
print(total)
print(sum(lst))
mx=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(mx)
min=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(min)