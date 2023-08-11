# def prime_number(num):
#     square_root = int(num**(1/2))
#     print(square_root)
#     for i in range(2, square_root):
#         if num % i == 0:
#             print('This number is not prime!')
#             break
#     else:

#         print('This number is prime!')


def sum_of_smaller_prime(num):
    sum = 0
    for smaller_num in range(2, num):
        square_root = int(smaller_num**(1/2))
        for number in range(2, square_root + 1):
            if smaller_num % number == 0:
                break
        else:
            sum += smaller_num
    return sum

print(sum_of_smaller_prime(24))