# Tabuada
def tabuada(x):
    for i in range(1, 11):
        res = x * i
        print('{} x {} = {}' .format(x, i, res))

while True:
    x = int(input('Digite um número para ver sua tabuada: '))
    print('Tabuada do ', x)
    tabuada(x)

    opcao = 0
    while(opcao != 1 and opcao != 2): # numero diferente de 1 e 2 repete a pergunta, 1 continua 2 encerra
        print('Deseja ver a tabuada de mais algum numero? (1-sim 2-não) ')
        opcao = int(input())

    if(opcao == 2): # encerra por conta dessa condição
        break