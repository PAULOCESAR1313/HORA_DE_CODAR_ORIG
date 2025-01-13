# PROGRAMAÇÃO ORIENTADA A OBJETOS - Onde cada linha serefere, ao um objeto do mundo, real. Esse paradigma é organizado em classes e objetos.
# Toda vez que eu for usar orientação a objeto, devo primeiro criar uma classe, ela vai serfir como molde para o meu objeto. Dessa forma podemos ter varios objetos basiados em um classe.
# Exemplo: Class pessoas - Essa classe pode ter caracteristicas e ações relacionados ao objeto.
#caracteristicas relacionadas a pessoas - Nome, idade, sexo, endereço, ocupação etc. As caracteristicas, também podem ser chamados de propriedade ou atribultos.
#ações relacionadas a pessoas - apresentação, tralho, etc. As ações também são conhecidas como método. Uma observação importante é que as classes podem ter tanto atributos e metodos, só um ou o outro. Não sendo Obrigatorio ter os dois ao mesmo tempo.
class pessoas:
    def __init__(self, nome, idade): # Ultilisando o atribulto self, eu consigo atribuir valor ao objto.
        self.nome = nome
        self.idade = idade
    
    def apresentacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos")
# Depois de criar a classe, precisamos criar o objto, porque só com a classe, não conseguimos rodar o codigo. E para criar ou instanciar um objto, precisamos primeiro criar uma variavel, depois atribuir a ela a classe e colocar os atributos da classe separados por virgulas. Ex: variavel = class(atributo, atributo, atributo)
    def aniversario(self): #Método aniversari - deve altera a idade do paulo += 1.
        self.idade +=1
        print(f"Fiz aniversario, agora tenno {self.idade} anos")

pessoa1 = pessoas("Paulo", 47) #Objeto pessoa1
pessoa1.apresentacao() #Método é a função do objto. objto.método() Como o método tem o atributo self, ele vai alto referenciar.
pessoa1.aniversario()
# Com a orientação a objeto, eu posso reaproveitar código, posso criar um objeto novo e reultilizar a classe e os métodos. Ex pessoa2.pessoas(nome, idade) - reutilizando a classe, pessoa2.apresentacao() - reutilizando o método.
pessoa2 = pessoas("Thayanne", 22)
pessoa2.apresentacao()
pessoa2.aniversario()

# Criar uma classe com o nome retangulo, com os atributos de altura e largura, depois criar um método que mostra a área do retangulo.

class retangulo:
    def __init__(self, altura, largura): # Ultilisando o atribulto self, eu consigo atribuir valor ao objto.
        self.altura = altura
        self.largura = largura