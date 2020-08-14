#speedtest.py
import time

x = 0

time_start = time.time()

while x < 50000:
    print(x)
    x += 1

print(f"{time.time() - time_start} seconds")

time.sleep(5)
