num = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыри', 'five': 'пять',
             'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
            'nine': 'девять', 'ten': 'десять'}

def num_translate(i):

    if i.istitle():
        return str(num.get(i.lower())).title()
    return num.get(i)



inter = input('enter the name of the number from 0 to 10: ')
print(num_translate(f'{inter}'))