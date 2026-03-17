mv = 9999999999
print("escreva [0] para sair")

while True:
    numero = int(input('\ndigite os numeros: '))
    if numero == 0:
        break
    if numero < mv:
        mv = numero
print("\no menor numero é: ", mv)