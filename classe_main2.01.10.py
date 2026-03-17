from heranca import Funcionario
from heranca import Gerente
if __name__ == '__main__':
    empregado1 = Funcionario("Baekhyun", 3000)
    gerente1 = Gerente("Rose", 20000, 2)
    print("\nEmpregado 1: ","\n Nome:", empregado1.get_nome(),"\n Salario: ", empregado1.get_salario())
    print("\nGerente 1: ","\n Nome:", gerente1.get_nome(),"\n Salario: ", gerente1.get_salario(),"\n Quantidade de funcionarios que grencia:", gerente1.get_quantidade_f())
    empregado1.set_nome("Baek-Hyun")
    empregado1.set_salario(3500)
    print("\nEmpregado 1 (valor alterado): ","\n Nome:", empregado1.get_nome(),"\n Salario:", empregado1.get_salario())
    gerente1.set_nome("Park Chaeyoung")
    gerente1.set_salario(10000)
    gerente1.set_quantidade_f(4)
    print("\nGerente 1 (valor alterado): ", "\n Nome:", gerente1.get_nome(), "\n Salario:", gerente1.get_salario(),
          "\n Quantidade de funcionarios que gerencia:", gerente1.get_quantidade_f())
    print("\n Bonus empregado1: ", empregado1.bonificacao())
    print("\n Bonus gerente 1: ", gerente1.bonificacao())