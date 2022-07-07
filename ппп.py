start_ls =[57.8, 46.51, 97, 76.05, 13.11, 87.93, 27, 97.09, 0.16, 42]

i = 0
while i < len(start_ls):
    if type(start_ls[i]) == int:
        start_ls[i] = float(start_ls[i])
    i += 1
print(start_ls)

x = 0
while x < len(start_ls):
    if type(start_ls[x]) == float:
        start_ls[x] = str(start_ls[x])
    x += 1
space = ' '
s_line = space.join(start_ls)
print(start_ls)
