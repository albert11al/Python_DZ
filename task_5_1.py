def nums_generator(n):

    for i in range(1, n+1, 2):
        yield i

print(*nums_generator(15))
