import time
import sys

done = 'false'
#here is the animation
def animate():
    while done == 'false':
        sys.stdout.write('\r  |   .Computing.   | ')
        time.sleep(0.1)
        sys.stdout.write('\r  /  . Computing .  / ')
        time.sleep(0.1)
        sys.stdout.write('\r  - .  Computing  . - ')
        time.sleep(0.1)
        sys.stdout.write('\r  \\  . Computing .  \\ ')
        time.sleep(0.1)

animate()
#long process here

sys.stdout.write('\r     Done!     ')
done = True