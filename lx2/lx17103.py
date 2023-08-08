import re
tt="The ghost that says boo huants the loo fgoo"
t=tt.replace(" ","\n")
m=re.findall(".*oo",t)

for a in m:
    print(a)

