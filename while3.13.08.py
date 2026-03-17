ct= 0
s = 0
print("\ndigite [-1] para sair da contagem")
c = str(input("\ndigite o nome da materia: "))
while True:
    nota = float(input('\ndigite a nota: '))
    if nota == -1:
        break
    ct = ct + 1
    s = s + nota
m = s/ct
print('\nmateria: ', c)
print('quantidade de alunos: ', ct)
print(f"media aritimedica da turma: {m:.2f}", m)
print('soma das notas dos alunos: ', s)