prices = [25.02, 50, 74.1, 96, 21.8, 20, 19.25, 1.25, 22.21, 22.65]
print(id(prices))
#A - Вывести цены в виде «5 руб 04 коп»
for i in prices:
    num = str(format(float(i), '.2f')).split('.')
    print(num[0], 'руб.', num[-1], 'коп.', end="/")
print(1)
#B - Вывести цены, отсортированные по возрастанию
print(sorted(prices))
print(id(prices))
#C Создать новый список, отсортированные по убыванию
new_my_list = sorted(prices, reverse=True)
print(new_my_list)
#D Вывести цены пяти самых дорогих товаров, по возрастанию
print(sorted(new_my_list[0:5]))



