from sys import argv
sales_lines = ['5978,5\n', '8914,3\n', '7879,1\n', '1573,7\n']
with open('bakery.csv', 'w', encoding='utf-8') as donut_r:
    donut_r.writelines(sales_lines)
with open("bakery.csv", "r", encoding="utf-8") as donut_r:
    if 1 < len(argv) < 4 and [i for i in argv[1:] if i.isdigit()]:
        if len(argv) == 3:
            start, finish = map(int, argv[1:])
            print(*(v for i, v in enumerate(donut_r) if start - 1 <= i < finish), sep="")
        else:
            print(*(v for i, v in enumerate(donut_r) if i >= int(argv[1]) - 1), sep="")
    else:
        print(donut_r.read())