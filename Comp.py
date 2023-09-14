from datetime import datetime
import time
import sys

start_time = datetime.now()

print("Loading:")

animation = [" 10% [■□□□□□□□□□]"," 20% [■■□□□□□□□□]", " 30% [■■■□□□□□□□]", " 40% [■■■■□□□□□□]", " 50% [■■■■■□□□□□]", " 60% [■■■■■■□□□□]", " 70% [■■■■■■■□□□]", " 80% [■■■■■■■■□□]", " 90% [■■■■■■■■■□]", "100% [■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")

a = int(1)
b = int(a)
c = int(a)
d = int(a)
e = int(a)
f = int(a)
g = int(a)
h = int(a)
i = int(a)
j = int(a)
k = int(a)
l = int(a)
m = int(a)
n = int(a)
o = int(a)
p = int(a)
q = int(a)
r = int(a)
s = int(a)
t = int(a)
u = int(a)
v = int(a)
w = int(a)
x = int(a)
y = int(a)
z = int(a)

XYZ = int(a)

coord = [[aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, ss, tt, uu, vv, ww, xx, yy, zz]
         for aa in range(a + 1)
         for bb in range(a + 1)
         for cc in range(a + 1)
         for dd in range(a + 1)
         for ee in range(a + 1)
         for ff in range(a + 1)
         for gg in range(a + 1)
         for hh in range(a + 1)
         for ii in range(a + 1)
         for jj in range(a + 1)
         for kk in range(a + 1)
         for ll in range(a + 1)
         for mm in range(a + 1)
         for nn in range(a + 1)
         for oo in range(a + 1)
         for pp in range(a + 1)
         for qq in range(a + 1)
         for rr in range(a + 1)
         for ss in range(a + 1)
         for tt in range(a + 1)
         for uu in range(a + 1)
         for vv in range(a + 1)
         for ww in range(a + 1)
         for xx in range(a + 1)
         for yy in range(a + 1)
         for zz in range(a + 1)

         if a+b+c+d+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z != XYZ]

now = datetime.now()

print(*coord, sep='\n')

print()

current_time = now.strftime("%H:%M:%S")
print("- Current Time =", current_time)
# print()
end_time = datetime.now()
print('-- Duration: {}'.format(end_time - start_time))