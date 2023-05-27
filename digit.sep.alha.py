def myfunc(num):
    for i in num:
        if num[i] == 3 or num[i+1]==3:
            return True
    
    return False

myfunc([1,3,3])
