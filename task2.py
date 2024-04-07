from math import sqrt
a = []
list_1 = int(input("Введите количество чисел 1 строки: "))
for z in range(list_1):
    new_n = int(input("Введите число: "))
    a.append(new_n)
print('Строка а - ',a)

b = []
list_2 = int(input("Введите количество чисел 2 строки: "))
for z in range(list_2):
    new_n = int(input("Введите число: "))
    b.append(new_n)
print('Строка b - ',b)

def task2 (a, b):
    if sum(a) == 0:
         print ('Нулевые данные проверить невозможно')
    elif sum(b) == 0:
         print ('Нулевые данные проверить невозможно')
    else:
        if list_1 > list_2:
            min = list_1 - list_2
            b2 = [0]*min
            b.extend(b2)
        elif list_2 > list_1:
            min = list_2 - list_1
            a2 = [0]*min
            a.extend(a2)
        
        i = 0
        sc = 0
        norm_a = 0
        norm_b = 0
        for z in range(list_1):
            sc_1 = a[i]*b[i]
            sc = sc_1 + sc
            norm_1_a = a[i]**2
            norm_a = norm_1_a + norm_a
            norm_1_b = b[i]**2
            norm_b = norm_1_b + norm_b
            i += 1
        norm_f = sqrt(norm_a)*sqrt(norm_b)
        cos_sim = sc/norm_f
        if cos_sim < 0:
            print ('Косинус не может быть меньше 0 - сходство нулевое')
        elif cos_sim > 1:
            print ('Косинус не может быть больше 1')
        else: 
            print (cos_sim)
task2 (a, b)



