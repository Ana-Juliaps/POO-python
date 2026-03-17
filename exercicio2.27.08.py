e = 0
n3 = 0
n4 = 0
def calcula_soma (n1, n2):
    soma = n1 + n2
    return soma
def calcula_subtrai (n1, n2):
    subtrai = n1 - n2
    return subtrai

if __name__ == '__main__':
    n1 = float(input("\nDigite o primeiro valor: "))
    n2 = float(input("\nDigite o segundo valor "))
    n3 = float(input("\nDigite o terceiro valor: "))
    n4 = float(input("\nDigite o quarto valor "))
    e = str(input("\nEscolha '+' para somar e '-' para subitrair: "))
    if e == '+':
        resultado = calcula_soma(n1, n2) + calcula_soma(n3, n4)
        print("\nA soma dos valores é: ", resultado)
    elif e == '-':
        resultado = calcula_subtrai(n1, n2) - calcula_subtrai(n3, n4)
        print("\nA subtração dos valores é: ", resultado)
    else:
        print("\nEscolha invalida")