# Juft son bor yoki yo'qligini tekshirish
# 1-usul:
""" sonlar = [1, 3, 5, 7]
juft_son_bormi = False
for son in sonlar:
    if son % 2 == 0:
        juft_son_bormi = True

if juft_son_bormi:
    print("Juft son bor ekan!")
else:
    print("juft son topilmadi!") """

# 2-usul:
sonlar = [1, 3, 5, 7]
for son in sonlar:
    if son % 2 == 0:
        print("Juft son bor ekan!")
        break
else: # for va while tsikllari bn else ishlataolamiz!
    print("Juft son topilmadi!")