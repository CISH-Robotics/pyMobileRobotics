from oclock import Timer
import time

timer = Timer(interval=0.02)  # Loops will be of total duration 2 seconds
lastTime = time.time()
while True:
    print(time.time() - lastTime)
    lastTime = time.time()
    timer.checkpt()