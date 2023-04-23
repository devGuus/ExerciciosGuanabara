vl = float(input('Qual é o salário do funcionario? R$'))
aumento = vl + (vl * 15 / 100)
totalaumento = (vl * 15 / 100)
print('Ele recebia R${}, com o auento de 15% vai receber R${:.2f}\nTotal do aumento R${:.2f}' .format(vl, aumento, totalaumento))