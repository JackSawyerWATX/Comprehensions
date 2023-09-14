from datetime import datetime
import time
import sys

print("Loading:")


# animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = [" 10% [■□□□□□□□□□]"," 20% [■■□□□□□□□□]", " 30% [■■■□□□□□□□]", " 40% [■■■■□□□□□□]", " 50% [■■■■■□□□□□]", " 60% [■■■■■■□□□□]", " 70% [■■■■■■■□□□]", " 80% [■■■■■■■■□□]", " 90% [■■■■■■■■■□]", "100% [■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")
#long process here

start_time = datetime.now()

a = int(1)
b = int(a)
c = int(b)
d = int(c)
e = int(d)
f = int(e)

n = int(a)

coord = [[a, b, c, d, e, f] 
         
         for aa in range(a + 1)
         for bb in range(b + 1)
         for cc in range(c + 1)
         for dd in range(d + 1)
         for ee in range(e + 1)
         for ff in range(f + 1)

          if aa + bb + cc + dd + ee + ff != n]


now = datetime.now()

print(*coord, sep='\n')

print()

current_time = now.strftime("%H:%M:%S")
print("- Current Time =", current_time)
# print()
end_time = datetime.now()
print('-- Duration: {}'.format(end_time - start_time))
done = 'true'
