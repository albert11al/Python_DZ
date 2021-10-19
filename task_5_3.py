from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Хусейн', 'Якуб']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

iterator = zip_longest(tutors, klasses[:len(tutors)])
print(tuple(iterator))

