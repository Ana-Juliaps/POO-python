from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    contador = 0
    def __init__(self, cor):
        self.cor = cor
        FormaGeometrica.contador = FormaGeometrica.contador + 1
    def get_cor(self):
        return self.cor
    def set_cor(self, nova_cor):
        self.cor = nova_cor
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
    @classmethod
    def get_contador(cls):
        return cls.contador

class Quadrado(FormaGeometrica):
    def __init__(self, cor, lado=2):
        super().__init__(cor)
        self.lado = lado
    def get_lado(self):
        return self.lado
    def set_lado(self, novo_lado):
        self.lado = novo_lado
    def area(self):
        vl_area = self.lado * self.lado
        return vl_area
    def perimetro(self):
        vl_perimetro = self.lado * 4
        return vl_perimetro
class Circulo(FormaGeometrica):
    def __init__(self, cor, raio=1):
        super().__init__(cor)
        self.raio = raio
    def get_raio(self):
        return self.raio
    def set_raio(self, novo_raio):
        self.raio = novo_raio
    def area(self):
        vl_area = 3.14 * (self.raio**2)
        return vl_area
    def perimetro(self):
        vl_perimetro = 2 * 3.14 * self.raio
        return vl_perimetro