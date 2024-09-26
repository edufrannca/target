# README - Questões Técnicas
## Descrição

Este projeto contém a implementação em **Python** para cinco questões técnicas comuns em entrevistas de desenvolvimento de software. Cada questão envolve um problema lógico ou de programação, variando de verificação de pertencimento à sequência de Fibonacci a desafios de lógica e controle de dispositivos (interruptores e lâmpadas).

---

## Índice

1. [Verificação de Pertencimento à Sequência de Fibonacci](#questão-1)
2. [Verificação de Ocorrências da Letra 'a' em uma String](#questão-2)
3. [Cálculo de Soma em Loop](#questão-3)
4. [Completar a Sequência Numérica](#questão-4)
5. [Problema dos Interruptores e Lâmpadas](#questão-5)

---

## Questão 1

### **Descrição:**

Dado um número, o programa verifica se ele pertence à sequência de Fibonacci, que começa com 0 e 1, e o próximo valor é sempre a soma dos dois anteriores (por exemplo: 0, 1, 1, 2, 3, 5, 8, 13...).

### **Como executar:**

1. Execute o script `pertence_fibonacci.py`.
2. Informe um número quando solicitado.
3. O programa retornará se o número informado pertence ou não à sequência de Fibonacci.

```bash
python pertence_fibonacci.py
```

---

## Questão 2

### **Descrição:**

O programa verifica quantas vezes a letra 'a', seja maiúscula ou minúscula, aparece em uma string informada. O usuário pode fornecer qualquer string para análise.

### **Como executar:**

1. Execute o script `conta_letras_a.py`.
2. Informe uma string quando solicitado.
3. O programa retornará a quantidade de vezes que a letra 'a' aparece na string, ou informará que ela não está presente.

```bash
python conta_letras_a.py
```

---

## Questão 3

### **Descrição:**

Um trecho de código em loop calcula o valor final de uma variável chamada `SOMA`, incrementando a variável `K` e somando seu valor a cada iteração, até que `K` seja maior que 12. Este programa simplesmente calcula e exibe o valor final de `SOMA`.

### **Como executar:**

1. Execute o script `calcula_soma.py`.
2. O programa retornará o valor final da variável `SOMA` ao final do processamento.

```bash
python calcula_soma.py
```

---

## Questão 4

### **Descrição:**

O programa propõe a identificação de padrões em diferentes sequências numéricas e, em seguida, completa o próximo valor de cada uma.

### **Sequências e Lógica:**

- **a)** `1, 3, 5, 7, ___` - Próximo número: `9` (incremento de 2)
- **b)** `2, 4, 8, 16, 32, 64, ____` - Próximo número: `128` (multiplica por 2)
- **c)** `0, 1, 4, 9, 16, 25, 36, ____` - Próximo número: `49` (quadrados perfeitos)
- **d)** `4, 16, 36, 64, ____` - Próximo número: `100` (quadrado de números pares)
- **e)** `1, 1, 2, 3, 5, 8, ____` - Próximo número: `13` (sequência de Fibonacci)
- **f)** `2, 10, 12, 16, 17, 18, 19, ____` - Próximo número: `20` (sequência mista de pares e ímpares)

### **Como executar:**

1. Execute o script `sequencias.py`.
2. O programa exibirá a lógica de cada sequência e o próximo número correspondente.

```bash
python sequencias.py
```

---

## Questão 5

### **Descrição:**

Este é um desafio de lógica onde você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. O objetivo é descobrir qual interruptor controla qual lâmpada com apenas duas idas até uma das salas das lâmpadas. A estratégia detalhada explica como alcançar esse objetivo de forma eficiente.

### **Como funciona:**

1. Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.
2. Desligue o primeiro interruptor e ligue o segundo.
3. Vá até a sala das lâmpadas:
   - A lâmpada acesa é controlada pelo segundo interruptor.
   - A lâmpada apagada e quente é controlada pelo primeiro interruptor.
   - A lâmpada apagada e fria é controlada pelo terceiro interruptor.

---

## Requisitos

- Python 3.x instalado na máquina
- Não é necessário instalar bibliotecas adicionais

---

## Instruções para Execução

1. Clone este repositório.
2. Navegue até o diretório do projeto.
3. Execute cada arquivo Python conforme descrito em cada questão, usando os comandos fornecidos.

---

## Autor

Este conjunto de questões foi desenvolvido para a entrevista técnica da **Target Sistemas**.
