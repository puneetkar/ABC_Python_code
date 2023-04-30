print('*'*30)
n1=input('Enter the user name: ').lower()
n1=(input('Enter the Password: '))
n3=input('Enter the Iteam you want to purchage:')
item=['glass','tv','perfume','router','speaker']
for v in n3:
    if item!=v:
        print('Print item avialable')
    else:
        print('Item not avaiable')