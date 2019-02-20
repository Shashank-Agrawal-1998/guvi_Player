s = input()
s1 = ''
lis = ['a','e','i','o','u']
for i in range(len(s)-1,-1,-1):
    if s[i].lower() not in lis:
        s1 = s1 + s[i]
print(s1)