ct = 0
n = 0
print('digite [-1] para sair da repetição')
while True:
      numero = int(input("Digite os numeros para contar: "))
      if numero == -1:
          break
      ct = ct + 1
      n =  n + numero
print('quantidade de números digitados: ', ct)
print('soma dos numeros: ', n)