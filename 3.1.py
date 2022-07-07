key = input('Введите значение: ')

w_tr = { "zero": "ноль",
         "one": "один",
         "two": "два",
         "three": "три",
         "four": "четире",
         "five": "пять",
         "six": "шесть",
         "seven": "семь",
         "eight": "восемь",
         "nine": "девять",
}

def num_translate(key):
    return print(w_tr.get(key))

num_translate(key)

