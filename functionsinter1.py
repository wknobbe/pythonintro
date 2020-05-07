import random
def rand_int(min = 0, max = 100):
    if min < 0:
        return False
    if min > max:
        return False
    if max < 0:
        return False
    if min == max:
        return min
    else:
        num = random.random() * (max-min) + min
        return num
print(rand_int())
print(rand_int(min = 50))
print(rand_int(max = 50))
print(rand_int(min = 50, max = 50))
print(rand_int(min = -1))
print(rand_int(max = -1))
print(rand_int(min = 20, max = 1))
print(rand_int(min = 100, max = 1000))