def nums_generator(n):
    nums = []
    for i in range(1, n+1, 2):
        nums.append(i)
    return nums

print(*nums_generator(15))