price_list = [57.7, 86, 46.51, 97, 10345.52, 48.15, 53.4, 83.05, 91.16, 1999.09, 204.37, 502, 170.44, 703.99, 1400.23]


def to_fixed(num_obj):
    str_obj = f"{num_obj:.{2}f}"
    str_obj = f"{str_obj[:-3]} руб {str_obj[-2:]} коп"
    return str_obj

print(', '. join(list(map(to_fixed, price_list))))

price_list.sort()
print(price_list)
new_price_list = sorted(price_list, reverse= True)
print(new_price_list)

i = 4
while i >= 0:
    print(new_price_list[i])
    i -= 1
