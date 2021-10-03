number = range(1, 1000, 2)
cube_number = []
n_sum = 0
all_sum = 0
for i in number:
    cube_number.append(i ** 3)
for n in cube_number:
    a_copy = n
    n_sum = 0
    while n > 0:
        n_sum += n % 10
        n //= 10
    if n_sum % 7 == 0:
        all_sum += a_copy
print(all_sum)
b_sum = 0
new_all_sum = 0
for n in cube_number:
    b = n + 17
    b_copy = b
    b_sum = 0
    while b > 0:
        b_sum += b % 10
        b //= 10
    if b_sum % 7 == 0:
        new_all_sum += b_copy
print(new_all_sum)