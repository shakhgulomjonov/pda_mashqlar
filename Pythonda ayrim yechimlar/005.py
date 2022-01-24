# 1-usul:
""" juft_sonlar = []
for son in range(1, 100):
    if son % 2 == 0:
        juft_sonlar.append(son)

for juft_son in juft_sonlar:
    print(juft_son ** 2) """

# 2-usul:
def juft_sonlar(b):
    for i in range(1, b):
        if i % 2 == 0:
            yield i


for juft_son in juft_sonlar(100):
    print(juft_son ** 2)