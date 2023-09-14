from datetime import datetime
import time
import sys

print()

done = 'false'
# here is the animation


print("Loading Application:")


# animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = [" 10% [■□□□□□□□□□]"," 20% [■■□□□□□□□□]", " 30% [■■■□□□□□□□]", " 40% [■■■■□□□□□□]", " 50% [■■■■■□□□□□]", " 60% [■■■■■■□□□□]", " 70% [■■■■■■■□□□]", " 80% [■■■■■■■■□□]", " 90% [■■■■■■■■■□]", "100% [■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")
# long process here

start_time = datetime.now()

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

n = int(a)

coord = [[a, b, c, d, e, f, g, h, i, j, k, l, m, o, p, q, r, s, t, u, v, w, x, y, z]

         for aa in range(a + 1)
         for bb in range(b + 1)
         for cc in range(c + 1)
         for dd in range(d + 1)
         for ee in range(e + 1)
         for ff in range(f + 1)
         for gg in range(g + 1)
         for hh in range(h + 1)
         for ii in range(i + 1)
         for jj in range(j + 1)
         for kk in range(k + 1)
         for ll in range(l + 1)
         for mm in range(m + 1)
         for oo in range(o + 1)
         for pp in range(p + 1)
         for qq in range(q + 1)
         for rr in range(r + 1)
         for ss in range(s + 1)
         for tt in range(t + 1)
         for uu in range(u + 1)
         for vv in range(v + 1)
         for ww in range(w + 1)
         for xx in range(x + 1)
         for yy in range(y + 1)
         for zz in range(z + 1)

         if aa + bb + cc + dd + ee + ff + gg + hh + ii + jj + kk + ll + mm  + oo + pp + qq + rr + ss + tt + uu + vv + ww + xx + yy + zz != n]

now = datetime.now()

print(*coord, sep='\n')

print()

current_time = now.strftime("%H:%M:%S")
print("- Current Time =", current_time)
# print()
end_time = datetime.now()
print('-- Duration: {}'.format(end_time - start_time))

done = True
sys.stdout.write('\rDone!     ')

