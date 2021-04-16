import re
# x="[abc]"       #either a or b or c
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#    print(match.start(),match.group())

# x="[^abc]"       #all except a or b or c
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#    print(match.start(),match.group())

# x="[a-z]"       #either a or b or c   [a-zA-Z] all a-z and A-Z all cap and small
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#    print(match.start(),match.group())

# x="\s"       #check space
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#    print(match.start(),match.group())

x="\w"       #either a or b or c
matcher=re.finditer(x,"abt c@5kz")
for match in matcher:
   print(match.start(),match.group())