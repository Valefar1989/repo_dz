new_ls = list(range(1,1001,2))
cub_ls = []
cub_ls_17 = []
total = 0
for i in new_ls:
    cub_ls.append(i**3)
print(cub_ls)
for i in range(len(cub_ls)):
    ind_cub = cub_ls[i]
    total_cub = 0
    while ind_cub != 0:
        total_cub += ind_cub % 10
        ind_cub = ind_cub // 10
    if total_cub % 7 == 0:
        total += cub_ls[i]
print(total)
total = 0

for i in new_ls:
    cub_ls_17.append(i**3 + 17)
print(cub_ls_17)
for i in range(len(cub_ls_17)):
    ind_cub = cub_ls_17[i]
    total_cub = 0
    while ind_cub != 0:
        total_cub += ind_cub % 10
        ind_cub = ind_cub // 10
    if total_cub % 7 == 0:
        total += cub_ls_17[i]
print(total)
