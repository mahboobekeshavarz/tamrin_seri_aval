my_list1 = [1, 2, 'a', 's', 20, 3, 7]
my_list2 = [3, 'a', 2, 5, 'b', 'd', 9]

def non_duplicate_num(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    set1.symmetric_difference_update(set2)
    non_duplicate_number = list(set1)
    return non_duplicate_number

print(non_duplicate_num(my_list1, my_list2))