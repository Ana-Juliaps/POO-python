from classe_abstrata_1211 import Employee, Fulltime, Hourly

if __name__ == '__main__':
    E1 = Fulltime("Rose", "Park", 20000)
    E2 = Fulltime("Hyunjin", "Hwang")
    print("\n\n Empoyee 1: ", E1, "\n Nome: ", E1.full_name(), "\n Salario:", E1.base_salary, "\n Salario + Bonus:", E1.compute_salary())
    print("\n\n Empoyee 1: ", E2, "\n Nome: ", E2.full_name(), "\n Salario:", E2.base_salary, "\n Salario + Bonus:",E2.compute_salary())
    E3 = Hourly("Rose", "Park", 200, 50)
    print("\n\n Empoyee 1: ", E3, "\n Nome: ", E3.full_name(), "\n Salario:", E3.compute_salary())
    print("\n\n Funcionarios: ", Employee.contador)