import random
m = random.choices(range(1, 1000, 1), k = 20)
def uni_mass(m):
    uni_f = []
    uni = []
    for x in m:
        if x not in uni:
            uni.append(x)
    uni_f = sorted(uni)
    print (uni_f)
uni_mass(m)
 
