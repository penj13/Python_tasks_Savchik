from math import sqrt

vector_a = [1, 0, 0]
vector_b = [1, 0, 0]
num_of_values_a = len(vector_a)
num_of_values_b = len(vector_b)


def cosine_similarity (a, b):
    if num_of_values_a == num_of_values_b:
        i = 0
        general_dot = 0
        general_norm_a = 0
        general_norm_b = 0
        for count_i in range(num_of_values_a):
            dot_i = a[i]*b[i]
            general_dot += dot_i
            norm_a_i = a[i]**2
            general_norm_a += norm_a_i
            norm_b_i = b[i]**2
            general_norm_b += norm_b_i
            i += 1
        general_norm = sqrt(general_norm_a)*sqrt(general_norm_b)
        cos_sim = general_dot/general_norm
        if cos_sim < -1:
            print ('Косинус не может быть меньше -1')
        elif cos_sim > 1:
            print ('Косинус не может быть больше 1')
        else: 
            print (cos_sim)
    else:
        print ('Разное количество значений в векторах')


cosine_similarity (vector_a, vector_b)
