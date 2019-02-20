s = input().strip()
s1 = ''
for i in s:
    i = ord(i)+3
    if i>122:
        i -= 26
    elif 90<i<94:
        i -= 26
    s1 = s1 + chr(i)
print(s1)