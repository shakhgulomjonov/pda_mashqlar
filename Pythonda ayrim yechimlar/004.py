# 1-usul:
"""class Tesla:
    motorlar_soni = 2
    maksimal_tezligi = 200
    modeli = "Model S"


mashinam = Tesla()
print("Oldin: ", mashinam.modeli)
mashinam.modeli = "Model X"
print("Keyin: ", mashinam.modeli) """

# 2-usul:
class Tesla:
    motorlar_soni = 2
    maksimal_tezligi = 200
    modeli = "Model S"


mashinam = Tesla()
maydon_nomi = input("Maydon nomini kiriting: ")
print("Oldin: ", mashinam.__getattribute__(maydon_nomi))
yangi_qiymat = input(f"{maydon_nomi} maydoni uchun yangi qiymat kiriting: ")
mashinam.__setattr__(maydon_nomi, yangi_qiymat)
print("Keyin: ", mashinam.__getattribute__(maydon_nomi))

# konsolga birinchi "maksimal_tezligi" jumlasi kiritiladi!