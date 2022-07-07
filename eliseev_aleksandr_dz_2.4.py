new_ls = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in new_ls:
    normal_name = i.split()[-1].capitalize()
    print(f"Привет, {normal_name}!")

