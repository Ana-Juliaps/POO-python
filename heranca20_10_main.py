from heranca29_10 import ContaCorrente, PessoaFisica, PessoaJuridica

if __name__ == '__main__':
    PessoaFisica1 = PessoaFisica("Bangchan", 2000000, "M")
    PessoaFisica2 = PessoaFisica("Rose", 2382900, "F")
    PessoaJuridica1 = PessoaJuridica("StrayKids", 927000000, "LTDA")
    PessoaJuridica2 = PessoaJuridica("BlackPink", 375000000, "MEI")
    print("\n Pessoa Física 1:", PessoaFisica1.get_nome(), "\n Saldo: R$",PessoaFisica1.get_saldo(), "\n Genero:", PessoaFisica1.get_genero())
    print("\n Pessoa Física 2:", PessoaFisica2.get_nome(), "\n Saldo: R$",PessoaFisica2.get_saldo(), "\n Genero:",PessoaFisica2.get_genero())
    print("\n\n Pessoa Jurídica 1:", PessoaJuridica1.get_nome(), "\n Saldo: R$", PessoaJuridica1.get_saldo(), "\n Modalidade:",PessoaJuridica1.get_modalidade())
    print("\n Pessoa Jurídica 2:", PessoaJuridica2.get_nome(), "\n Saldo: R$", PessoaJuridica2.get_saldo(),"\n Modalidade:", PessoaJuridica2.get_modalidade())
    PessoaFisica1.deposito(2000)
    print("\n Pessoa Física 1:", PessoaFisica1.get_nome(), "\n Saldo: R$", PessoaFisica1.get_saldo())
    PessoaJuridica2.saque(25800)
    print("\n Pessoa Jurídica 2:", PessoaJuridica2.get_nome(), "\n Saldo: R$", PessoaJuridica2.get_saldo())
    PessoaFisica2.saque(2382901)
