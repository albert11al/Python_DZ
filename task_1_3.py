number = range(1, 101, 1)
percent = ['процентов', 'процент', 'процента']
for n in number:
    if n % 10 == 1 and not n == 11:
        print(n, percent[1])
    elif 4 >= n % 10 >= 2 and not 14 >= n >= 12:
        print(n, percent[2])
    else:
        print(n, percent[0])