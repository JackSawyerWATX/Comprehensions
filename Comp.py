from datetime import datetime

start_time = datetime.now()

u = int(input('First Parameter: '))
v = int(input('Second Parameter: '))
w = int(input('Third Parameter: '))
x = int(input('Fourth Parameter: '))
y = int(input('Fifth Parameter: '))
z = int(input('Sixth Parameter: '))
n = int(input('LAST Parameter: '))

coord = [[f, g, h, i, j, k] 
         for f in range(x + 1)
         for g in range(x + 1)
         for h in range(x + 1)
         for i in range(x + 1) 
         for j in range(y + 1) 
         for k in range(z + 1) 
         if f + g + h + i + j + k != n]

now = datetime.now()

print(*coord, sep='\n')

print()

current_time = now.strftime("%H:%M:%S")
print("- Current Time =", current_time)
print()
end_time = datetime.now()
print('-- Duration: {}'.format(end_time - start_time))