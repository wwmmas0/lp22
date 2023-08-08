import re
tt="Arizona 479、501、870.Carlifornia 209、213、650．"
m=re.findall("\d",tt,re.IGNORECASE)
print(m)
