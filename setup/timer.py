import time
timer = False
second = 31
if timer == True:
    for i in range(30,0,-1):
        second = i
        time.sleep(1)
        print(i)
    timer = False
