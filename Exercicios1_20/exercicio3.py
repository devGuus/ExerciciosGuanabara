palavra = input("Digite algo: ")
print("O tipo primitivo dessa palavra é ", type(palavra))
print("Somente espaços? ", palavra.isspace())
print("É um número? ", palavra.isnumeric())
print("É alfabetico? ", palavra.isalpha())
print("É alfanumerico? ", palavra.isalnum())
print("Estão em maiúsculas? ", palavra.isupper())
print("Estão em minúsculas? ", palavra.islower())
print("Está captalizada? ", palavra.istitle())