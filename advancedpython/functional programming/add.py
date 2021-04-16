#add numbers
# add=lambda num1,num2:num1+num2
# print(add(1,2))


#map()
#filter()
#reduce()

#map()
#2 arguments
#1 function
#2 iterables
lst=[10,20,30,21,22,24]
squ=list(map(lambda n:n**2,lst))
print(squ)
cube=list(map(lambda n:n**3,lst))
print(cube)