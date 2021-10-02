time = int(input('Введи время в секундах: '))
if time < 60:
    print(time, 'сек')
elif 3600 > time > 60:
    minute = time // 60
    second = time % 60
    print(minute, 'мин', second, 'сек')
elif 86400 > time > 3600:
    hour = time // 3600
    minute = (time % 3600) // 60
    second = (time % 3600) % 60
    print(hour, 'час', minute, 'мин', second, 'сек')
elif time > 86400:
    day = time // 86400
    hour = (time % 86400) // 3600
    minute = ((time % 86400) % 3600) // 60
    second = ((time % 86400) % 3600) % 60
    print(day, 'дня', hour, 'час', minute, 'мин', second, 'сек')