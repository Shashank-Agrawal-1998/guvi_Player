s = input()
s1 = ''
for i in range(len(s)):
    if (i==0) or (s[i]!=' ' and s[i-1]==' '):
        s1 = s1 + s[i].upper()
    else:
        s1 = s1 + s[i].lower()
print(s1)