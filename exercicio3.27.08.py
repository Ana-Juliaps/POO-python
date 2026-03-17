mt = 0
def maximo(n1, n2):
    if n1 > n2:
        maior = n1
    elif n2 > n1:
        maior = n2
    else:
        print("valores são iguais")
    return maior

def mínimo(n1, n2):
    if n1 < n2:
        menor = n1
    elif n2 < n1:
        menor = n2
    else:
        print("valores são iguais")
    return menor

if __name__ == '__main__':
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("\nDigite o segundo número: "))
    m = maximo(n1, n2)
    n = mínimo(n1, n2)
    mt = maximo(5,7)
    print("\nO maior é: ", m)
    print("O menor é: ", n)
    print("O maior é: ", maximo(n1, n2)) #sem usar a variavel m e n
    print("O menor é: ", mínimo(n1, n2))  #sem usar a variavel m e n
    print("\nO maior é: ", mt) #chamar a função maximo duas vezes.