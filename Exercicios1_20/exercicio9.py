# conversão para dolar, valor do dia 17/04/2023
dollar = 4.94 # mude o valor do dollar aqui
real = float(input('Quanto de dinheiro você possui? '))
if real < 4.94:
    print('Está muito probre, cursou direito na faculdade?')
elif real >= 4.94:
    valor = real / dollar
    print('Com R${:.2f} você possui US{:.2f}' .format(real, valor))