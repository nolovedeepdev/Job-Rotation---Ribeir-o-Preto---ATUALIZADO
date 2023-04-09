num = int(input("Informe um número: "))

# Inicialização dos valores da sequência de Fibonacci
fib_ant_ant = 0  # Valor anterior ao anterior
fib_ant = 1  # Valor anterior
fib_atual = 1  # Valor atual

# Loop para gerar a sequência de Fibonacci até que o valor atual seja maior ou igual ao número informado pelo usuário
while fib_atual < num:
    fib_ant_ant = fib_ant
    fib_ant = fib_atual
    fib_atual = fib_ant_ant + fib_ant

# Verificação se o número informado pertence à sequência de Fibonacci
if fib_atual == num:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")
