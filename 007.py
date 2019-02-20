s = input()
s1 = ''
for i in range(0,len(s),2):
    s1 = s1 + s[i+1] + s[i]
print(s1)