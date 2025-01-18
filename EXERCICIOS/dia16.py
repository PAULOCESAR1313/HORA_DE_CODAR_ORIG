#Padrões de projeto - São formas de programar que trazem resultados benéficos para nossa aplicação, existe varios padros.
# SINGLETON - Ele garante que aclasse tenha apenas uma instacia. Dessa forma criamos varios objetos, 1, 2,3 ... 10 objetos ele funcionam como se fosse uma coisa só.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls) # Basicamento estou transformando cada objto novo em um Singleton.
            print("Instancia Singleton foi criado!")
        return cls._instance
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)

#PADRÃO FACTORY (FABRICA) - Ele define uma interface para criar objtos mas, permite que subclasses decidam qual objeto criar. Ou seja o padão FACTORY É considerado uma fabrica de objtos.

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass # Comando que permite acriação de subclasses
  

# FABRICA DE TRANSPORTE - criar: Carros e Barcos, mas precisa de um método chamado de mover para criar o objto.

class carro(Transporte):
    def mover(self):
        print("O carro está se movendo!")

class barco(Transporte):
    def mover(self):
        print("O barco está se movendo!")

class fabricaTransporte:
    def criar_transporte(self, tipo):
        if tipo == "caro":
            return carro()
        elif tipo == "barco":
            return barco()
        else:
            raise ValueError("Tipo de transporte invalido!")

fabrica = fabricaTransporte()

transp1 = fabrica.criar_transporte("carro")
transp2 = fabrica.criar_transporte("barco")
#transp3 = fabrica.criar_transport("aviao")

transp1.mover()
transp2.mover()
#transp3.mover()