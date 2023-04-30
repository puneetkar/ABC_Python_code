def myfunc(s):
    l=s.split()
    l1=l[::-1]
    output=' '.join(l1)
    print(output)

myfunc('python is very easy')