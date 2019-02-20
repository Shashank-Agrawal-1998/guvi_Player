n = int(input())
words = []
for i in range(n):
    words.append(input().strip().lower())
s = 'kabali'
ascii_s = ord('k') + ord('a') + ord('b') + ord('a') + ord('l') + ord('i')
c = 0
for word in words:
    if len(word)==len(s):
        ascii_sum = 0
        for i in word:
            ascii_sum += ord(i)
        if ascii_sum == ascii_s:
            c += 1
print(c)