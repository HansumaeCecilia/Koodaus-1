import time

aikaleima = time.time()
print(aikaleima)

aikateksti = time.ctime(aikaleima)
print(aikateksti)

aika1 = time.time()
time.sleep(3)

aika2 = time.time()

print(aika1)
print(aika2)
print(aika2 - aika1)