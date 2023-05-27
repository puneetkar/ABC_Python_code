s='AABBDDVVVVEEE'
d={}
output=''
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)

for k,v in d.item():
    out