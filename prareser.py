s=input('Enter the string :')
output=''
i=len(s)
while i>=0:
    output=output+s[i]
    i=i+1
print(output)

def myfunc(s):
    l=s.split()
    l1=l[::-1]
    output=''.join(l1)
    return output
