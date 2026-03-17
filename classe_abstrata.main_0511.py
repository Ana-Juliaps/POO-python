from classe_abstrata_0511 import FormaGeometrica, Quadrado, Circulo

if __name__ == '__main__':
    print("\n Contador: ", FormaGeometrica.contador)
    Q1 = Quadrado("Rosa")
    Q2 = Quadrado("Roxo", 4)
    print("\n Quadrado 1:",Q1,"\n   Cor:",Q1.get_cor(), "\n   Lado:", Q1.get_lado(), "\n   Perimetro:", Q1.perimetro(), "\n   Area:", Q1.area())
    print("\n Quadrado 2:", Q2, "\n   Cor:", Q2.get_cor(), "\n   Lado:", Q2.get_lado(), "\n   Perimetro:", Q2.perimetro(), "\n   Area:", Q2.area())
    C1 = Circulo("Amarelo", 7)
    C2 = Circulo("Preto")
    print("\n Círculo 1:", C1, "\n   Cor:", C1.get_cor(), "\n   Raio:", C1.get_raio(), "\n   Perimetro:",C1.perimetro(), "\n   Area:", C1.area())
    print("\n Círculo 2:", C2, "\n   Cor:", C2.get_cor(), "\n   Raio:", C2.get_raio(), "\n   Perimetro:",C2.perimetro(), "\n   Area:", C2.area())
    print("\n Contador: ", FormaGeometrica.contador)