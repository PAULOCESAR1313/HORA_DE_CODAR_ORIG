# MODULOS - São pacotes de funcinalidades, também chamados de biblioteca, que pode ou NÃO estarem instalados no PYTHON
# Quando eles estão instalados no python nós importamos, quando não estão, instalamos, usando o gerenciador de dependencia o pip

import math # MODULO DE MATEMATICA, BIBLIOTECA COMPLETA

numero = 16
raiz_quadrada = math.sqrt(numero)

print(f"A raiz quadrada de: {numero} é {raiz_quadrada}")

from math import pi # MODULO DE MATEMATICA - apenas uma funcionalidade.

print(f"O valor de pi é: {pi}") 

# OBS: Podemos importa um MODULO/BIBLIOTECA inteira ou apenas partes.
# Para importa de forma completa usamos o comando import.
# Para usar um a biblioteca por partes usamos: from nome da bibiloteca import o nome da funcionalidade.

# Ultilizando alias - São simplificação do nome da biblioteca

import math as m # A letra M esta representando de forma simplificada a biblioteca math.

print(f"O cosseno do número 0 é: {m.cos(0)}")

# OBS: OS IMPORTS DEVEM SER USADOS, PREFERENCIALMENTE NO TOPO DO CÓDIGO!

import random # BIBLIOTECA COMPLETA

dado = random.randint(1, 6)

print(f"O número sorteado é: {dado}")

# BIBLIOTECA PARA TRABALHAR COM DATAS

from datetime import datetime

agora = datetime.now()
print(agora)
