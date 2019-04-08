h1, m1 = map(int, input().strip().split())
h2, m2 = map(int, input().strip().split())

minute1 = h1*60 + m1
minute2 = h2*60 + m2

diff1 = abs(minute1 - minute2)

h = diff1//60
m = diff1 - h*60

print(h,m)
