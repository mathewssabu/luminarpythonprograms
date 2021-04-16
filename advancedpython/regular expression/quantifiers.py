#quantifiers
import re
# x="a+"
# r="aaa aabc a ddda"  #including a grp
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),match.group())

x="a*"
r="aaa aabc a ddda"  #count includig zero no. of a
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start(),match.group())
#
# x="a?"          #count a as each including zero no. of a
# r="aaa aabc a ddda"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),match.group())

# x="a{2}"  #no. of a position
# r="aaa aabc a ddda"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),match.group())

# x="a{1,3}"  #min 1 a and max 3 a
# r="aaa aabc a ddda"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),match.group())

# x="^a"  #check starting with a
# r="aaa aabc a ddda"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),match.group())

# x="a$"  #check string end with a
# r="aaa aabc a ddda"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),match.group())