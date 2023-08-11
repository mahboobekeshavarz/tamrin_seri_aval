def max_dict():
    A = ['a', 'a', 'a', 2, 3, 'a', 2, 4, 9, 3, 3, 'a']
    A_1 = set(A)
    D = {}
    for j in range(len(A_1) + 1):
        for i in A:
            num_of_i = 0
            for j in A:
                if i == j:
                    num_of_i += 1
            D[i] = num_of_i
            while i in A:
                A.remove(i)
            A_1 = set(A)
            D_sorted = sorted(D.items(), key=lambda x: x[1], reverse=True)
    # print(D_sorted)
    return D_sorted[0]


print(max_dict())