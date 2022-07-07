new_ls = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(new_ls):
    if new_ls [i].isdigit():
        new_ls[i] = new_ls[i].zfill(2)
    if new_ls[i].startswith('+') and (new_ls[i])[1:].isnumeric():
        new_ls[i] = new_ls[i].zfill(3)
    i += 1
print(new_ls)

space = ' '
new_st = space.join(new_ls)
print(new_st)