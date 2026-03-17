class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def get_nome(self):
        return self.nome
    def get_salario(self):
        return self.salario
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_salario(self, novo_salario):
        self.salario = novo_salario
    def bonificacao(self):
        bonus = self.salario * 0.1
        return bonus
class Gerente(Funcionario): #conceito de herança
    def __init__(self, nome, salario, quantidade_f):
        super().__init__(nome, salario)
        self.quantidade_f = quantidade_f
    def get_quantidade_f(self):
        return self.quantidade_f
    def set_quantidade_f(self, nova_quantidade):
        self.quantidade_f = nova_quantidade