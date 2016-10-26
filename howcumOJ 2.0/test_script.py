import time

now = time.time()
future = now + 1
while time.time() < future:
    print(time.time())
    pass