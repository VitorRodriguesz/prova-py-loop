soma = 0
quantidade_numeros = 0

# Loop para ler os números
while True:
    try:
        # Lê um número inteiro do teclado
        numero = int(input("Digite um número inteiro (0 para sair): "))

        # Se o número for 0, sai do loop
        if numero == 0:
            break

        # Adiciona o número à soma e incrementa a quantidade de números
        soma += numero
        quantidade_numeros += 1
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Calcula a média aritmética, evitando divisão por zero
media = soma / quantidade_numeros if quantidade_numeros > 0 else 0

# Exibe os resultados
print(f"Quantidade de números digitados: {quantidade_numeros}")
print(f"Soma dos números digitados: {soma}")
print(f"Média aritmética dos números digitados: {media}")
