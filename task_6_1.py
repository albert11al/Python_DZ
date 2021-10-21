file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')

content = ((i.split()[0], i.split()[5][1:], i.split()[6]) for i in file_1)
for n in content:
    print(n)
