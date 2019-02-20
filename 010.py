s1, s2 = map(str, input().strip().split())
differ = 0
n = len(s1)
for i in range(n):
    if s1[i] != s2[i]:
        differ += 1
    if differ>2:
        break
if differ==1:
    print('yes')
else:
    print('no')