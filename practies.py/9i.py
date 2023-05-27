a='a2m3c4e2b4'
d=''
target=''
for ch in a:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        target=target+x*d
print(target)
print(''.join(sorted(target)))