#pattern matching
#re --package for pattern matching

import re
c=0
matcher=re.finditer('ab','abbababaab')
for match in matcher:
    print("match at",match.start())  #return position
    print(match.group())           #return which object to find
    c+=1
print(c)