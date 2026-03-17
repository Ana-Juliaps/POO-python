def calcula_dobro(p_valor):
    dobro = p_valor * 2
    return dobro
if __name__ == '__main__': #digitar main e depois tab
    valor = int(input("Valor inteiro: "))
    v_retornado = calcula_dobro(valor)
    print("valor retornado pela função:", v_retornado) #modo 1
    print("valor retornado pela função: ", calcula_dobro(valor)) #modo 2