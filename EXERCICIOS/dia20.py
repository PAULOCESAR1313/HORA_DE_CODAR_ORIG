# BOAS PRATICAS DE PROGRAMAÇÃO - Seguindo os padroes Clean code. Para isso o código deve estar, bem comentado, facilitando a manutenção por terceiros, o código de ver limpo, sem redundancias.

"""
 A função abaixo calcula media de notas e ela vai ter parâmetros e vai ser estipulado um retorno

 Parêmetros:
        notas (lista) - Essa lista vai conter as notas

 Retorno:
        média (float): Vai me mostrar o resultado, a média calculada.

"""

def calcular_media(notas):
    return sum(notas) / len(notas)
print(calcular_media({10, 3, 10}))