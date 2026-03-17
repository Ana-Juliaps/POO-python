menor = 99999999
maior = -9999999
print("escreva [0] para sair")

while True:
    numero = int(input('\ndigite os numeros: '))
    if numero == 0:
        break
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
print("\no menor numero é: ", menor)
print("\no maior numro é: ", maior)
