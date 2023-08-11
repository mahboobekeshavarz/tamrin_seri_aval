a = ['a', 'a', 'a', 2, 3, 'a', 2, 4, 9, 'b', 3, 'b', 3, 'a']

def twice(my_list):
    D = {}
    l = []
    for j in range(len(my_list) + 1):
        for i in my_list:
            num_of_i = 0
            for j in my_list:
                if i == j:
                    num_of_i += 1
            D[i] = num_of_i
    # print(D)
    for key, value in D.items():
        if value == 2:
            l.append(key)
    return l
    

print(twice(a))