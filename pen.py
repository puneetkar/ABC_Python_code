s='b4a1d3'
alphabets=[]
digit=[]

for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digit.append(ch)
    output=''.join(sorted(alphabets)+sorted(digit))
print(output)