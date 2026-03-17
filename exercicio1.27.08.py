print("\nClcular dois valores")
def calcula_soma (n1, n2):
    soma = n1 + n2
    return soma

if __name__ == '__main__':
    n1 = float(input("\nDigite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    resultado = calcula_soma (n1, n2)
    print("\nA soma dos valores é: ", resultado)
    print("A soma dos valores é: ", calcula_soma(2.1, 3.5))