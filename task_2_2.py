my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list = ' '.join(my_list)
new_my_list = []
num = ''
for i in my_list:
    if i.isdigit():
        num += i
    else:
        if num != '':
            new_my_list.append(int(num))
            num = ''
my_list = my_list.split(" ")
for i, n in enumerate(my_list):
    if n == f'{my_list[1]}':
        my_list[i] = f'"{"{:02d}".format(new_my_list[0])}"'
    elif n == f'{my_list[3]}':
        my_list[i] = f'"{"{:02d}".format(new_my_list[1])}"'
    elif n == f'{my_list[8]}':
        my_list[i] = f'"{"{:+03d}".format(new_my_list[2])}"'
print(' '.join(my_list))






