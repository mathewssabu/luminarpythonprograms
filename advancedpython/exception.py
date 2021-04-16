# a=int(input("enter 1"))
# b=int(input("enter 2"))
# c=a/b
# print(c)
# try:                               #a[x]
#     res=a/b                    #x<=2
#     print("res=",res)
# #except:
# except Exception as e :
#   print("exception  occured")
try:
     a = int(input("enter 1"))
     b = int(input("enter 2"))
     print(a/b)
except:
     print("entr an integer value")
finally:
     print("will execute always")