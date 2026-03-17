class ContaCorrente:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    def get_nome(self):
        return self.nome
    def get_saldo(self):
        return self.saldo
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def deposito(self, novo_deposito):
        if novo_deposito > 0:
            self.saldo = self.saldo + novo_deposito
        else:
            print("Erro valor negativo")
class PessoaFisica(ContaCorrente):
    def __init__(self, nome, saldo, genero='m'):
        super().__init__(nome, saldo)
        self.genero = genero
    def get_genero(self):
        return self.genero
    def set_genero(self, novo_genero):
        self.genero = novo_genero
    def saque(self, retirada):
        if retirada <= self.saldo:
            self.saldo = (self.saldo - retirada) - 2
        else:
            print("Valor insuficiente")

class PessoaJuridica(ContaCorrente):
    def __init__(self, nome, saldo, modalidade):
        super().__init__(nome, saldo)
        self.modalidade = modalidade
    def get_modalidade(self):
        return self.modalidade
    def set_modalidade(self, nova_modalidade):
        self.modalidade = nova_modalidade
    def saque(self, retirada):
        if retirada <= self.saldo:
            self.saldo = (self.saldo - retirada) - 5
        else:
            print("Valor insuficiente")