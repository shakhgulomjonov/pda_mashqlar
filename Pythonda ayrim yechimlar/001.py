from decimal import Decimal
# Decimal - bu kasr!

a, b, c = Decimal('0.1'), Decimal('0.2'), Decimal('0.3')
if a + b == c:
    print("0.1 + 0.2 = 0.3")
else:
    print("Nimadir xato ketdi!")