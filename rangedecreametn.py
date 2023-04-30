def myfunc(x):
    output=[]
    for i in range (len(x)):
        if i%2==0:
            output.append(x[i].upper())
        else:
            output.append(x[i].lower())
    print(output)

myfunc('puneet')