from datetime import datetime

x = int(input('First Parameter: '))
y = int(input('Second Parameter: '))
z = int(input('Third Parameter: '))
n = int(input('Fourth Parameter: '))

coord = [[i, j, k] 
         for i in range(x + 1) 
         for j in range(y + 1) 
         for k in range(z + 1) 
         if i + j + k != n]

now = datetime.now()

print(coord)

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)