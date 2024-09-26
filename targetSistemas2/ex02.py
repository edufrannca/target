def conta_letras_a(texto):
    quantidade = texto.lower().count('a')
    
    if quantidade > 0:
        return f"A letra 'a' aparece {quantidade} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

# Exemplo de uso
texto = input("Informe uma string: ")
print(conta_letras_a(texto))
