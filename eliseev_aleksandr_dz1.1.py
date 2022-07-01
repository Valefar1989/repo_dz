duration = int(input('Введите время в секундах: '))

if duration >= 86400:
    day = duration//86400
    rem_day = duration%86400
    hour = rem_day//3600
    rem_hour = rem_day%3600
    minutes = rem_hour//60
    seconds = rem_hour%60
    print(day, ' дн.', hour, ' ч.', minutes, ' мин.', seconds, ' сек.')

if duration < 86400 and duration >= 3600:
    hour = duration//3600
    rem_hour = duration%3600
    minutes = rem_hour//60
    seconds = rem_hour%60
    print(hour, ' ч.', minutes, ' мин.', seconds, ' сек.')

if duration < 3600 and duration >= 60:
    minutes = duration//60
    seconds = duration%60
    print(minutes, ' мин.', seconds, ' сек.')

if duration < 60:
    seconds = duration
    print(seconds, ' сек.')




