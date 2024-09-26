def pertence_fibonacci(numero):
    fibo = [0, 1]
    while fibo[-1] < numero:
        fibo.append(fibo[-1] + fibo[-2])

    if numero in fibo:
        return f"{numero} pertence à sequência de Fibonacci."
    else:
        return f"{numero} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))
