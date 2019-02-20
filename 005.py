s = input()
ans = 0
for i in s:
    if i=='X' or i=='x':
        ans = ans + 10
    elif i=='V' or i=='v':
        ans = ans + 5
    else:
        ans = ans + 1
print(ans)