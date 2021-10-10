from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n, flag=False):
    """
    Функция возращает случайные шутки, собранные из трех списков слов

    :param n: количество шуток
    :param flag: уникальные/неуникальные
    :return: список случайных шуток

    """
    for i in range(n):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke = f'{noun} {adverb} {adjective}'
        if flag:
            list = joke.split()

            for noun in nouns.copy():
                for fun in list:
                    if noun == fun:
                        nouns.remove(noun)

            for adverb in adverbs.copy():
                for fun in list:
                    if adverb == fun:
                        adverbs.remove(adverb)

            for adjective in adjectives.copy():
                for fun in list:
                    if adjective == fun:
                        adjectives.remove(adjective)
        print(joke)

get_jokes(4, True)