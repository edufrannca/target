def calcula_soma():
    indice = 12
    soma = 0
    k = 1

    while k < indice:
        k = k + 1
        soma = soma + k

    return soma

# Exemplo de uso
print(f"O valor final da variável SOMA é: {calcula_soma()}")
