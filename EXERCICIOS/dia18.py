#DEBUGGING - Debuggingar é encontrar erros no código, ou entender como o seu código esta funcionando
# Print - É uma forma de debungging. Não é considerado a melhor forma, mas é rapida, ao colocar o comando print, no caso de algum erro no código uma mensage vai aparecer e apontar o erro.

def dividir(a, b):
    print(f"Quanto é {a} dividido por {b}?")
    if b == 0:
        return None
    
    resultado = a / b
    print(f"O resultado de {a} / {b} é: {resultado}")
    return resultado
dividir(0 ,5)
dividir(10, 0)
