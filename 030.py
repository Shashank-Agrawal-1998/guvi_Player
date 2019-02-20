h1, m1 = map(int, input().strip().split())
h2, m2 = map(int, input().strip().split())

minute1 = h1*60 + m1
minute2 = h2*60 + m2

diff = abs(minute1 - minute2)

h = diff//60
m = diff - h*60

print(h,m)