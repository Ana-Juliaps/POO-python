class Aluno:
    def __init__ (self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_mensalidade(self):
        return self.mensalidade
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_mensalidade(self, nova_mensalidade):
        self.mensalidade = nova_mensalidade
    def set_idade(self, nova_idade):
        self.idade = nova_idade

if __name__ == '__main__':
    aluno1 = Aluno("Bangchan", 2143.00,27)
    aluno2 = Aluno("Hyunjin", 2143.00, 25)
    aluno3 = Aluno("Jisung", 1430.00, 23)
    aluno4 = Aluno("Félix", 2143, 24)
    print("Endereço hexadecimal do objeto 1:", aluno1)
    print("\nAluno 1: \nNome:", aluno1.get_nome(), "\nIdade:", aluno1.get_idade(), "\nMensalidade:", aluno1.get_mensalidade())
    print("\n\nAluno 2: \nNome:", aluno2.get_nome(), "\nIdade:", aluno2.get_idade(), "\nMensalidade:", aluno2.get_mensalidade())
    print("\n\nAluno 3: \nNome:", aluno3.get_nome(), "\nIdade:", aluno3.get_idade(), "\nMensalidade:", aluno3.get_mensalidade())
    print("\n\nAluno 4: \nNome:", aluno4.get_nome(), "\nIdade:", aluno4.get_idade(), "\nMensalidade:",aluno4.get_mensalidade())
    aluno3.set_nome("Han Jisung") #mudar nome
    aluno4.set_mensalidade(1430.00) #mudar a mensalidade
    print("\n\nAluno 3: \nNome:", aluno3.get_nome(), "\nIdade:", aluno3.get_idade(), "\nMensalidade:", aluno3.get_mensalidade())
    print("\n\nAluno 4: \nNome:", aluno4.get_nome(), "\nIdade:", aluno4.get_idade(), "\nMensalidade:",aluno4.get_mensalidade())