s='AAAADDDDEEEEFFF'
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1

output=''
for k,v in d.items():
    output=output+str(v)+k
print(output)