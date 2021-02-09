import time
import sys

i = 0

while 1:
    s = "_" * i + "-" + "_" * (10 - i)
    print(s, end='\r')
    sys.stdout.flush()
    i += 1
    i %= 10
    time.sleep(1)
