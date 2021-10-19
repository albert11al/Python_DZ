src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [more_than for i, more_than in zip(src, src[1:]) if more_than > i]
print(result)
# a = []
# for i, more_than in zip(src, src[1:]):
#    if more_than > i:
#        a.append(more_than)
# print(a)

