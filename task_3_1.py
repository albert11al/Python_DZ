def num_translate(i):
    print({'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыри', 'five': 'пять',
             'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
            'nine': 'девять', 'ten': 'десять'}.get(i, None))
    


inter = input('enter the name of the number from 0 to 10: ')
num_translate(f'{inter}')

