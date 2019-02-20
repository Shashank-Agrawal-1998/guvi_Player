s = input()
numeric = 0 
for i in range(len(s)):
    if not(48<=ord(s[i])<=57 or s[i]=='.'):
        numeric = 1
if numeric==0:
    print('yes')
else:
    print('no')