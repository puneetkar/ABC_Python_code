s='one two three four'
l=s.split()
l1=[]
i=0
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
print(l1)