s = input().strip()
d = {}
for i in s:
    i = i.lower()
    d[i] = d.get(i, 0) + 1
max_count = 0
max_letter = None
for i in d:
    if d[i] > max_count:
        max_count += 1
        max_letter = i
print(max_letter)