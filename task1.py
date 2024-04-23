import random
m = random.choices(range(1, 1000, 1), k = 20)
def uni_mass(m):
    uni_f = sorted(set(m))
    return uni_f
uni_mass(m)
