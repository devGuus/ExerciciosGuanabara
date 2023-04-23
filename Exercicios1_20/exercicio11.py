vl = float(input('Qual é o preço do produto? R$'))
desc = vl - (vl * 5 / 100)
totaldesc = (vl * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}\nTotal do desconto R${:.2f}' .format(vl, desc, totaldesc))