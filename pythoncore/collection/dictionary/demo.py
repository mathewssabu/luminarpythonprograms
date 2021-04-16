#dictionary
#key-value pairs
diction={"name":"arun","roll":1001,"age":25}
# for i in diction:
#     print(i,":",diction[i])
#support hetrogenous
#support dulicate value but not duplicate key
#insersion order preserved
#dictionary name["key"]
diction["name"]="mathews"   #updation
diction["age"]=30
for i in diction:
    print(i,":",diction[i])
#del delete keyword
del diction["age"]
print(diction)
diction["age"]=25
print("age"in diction)