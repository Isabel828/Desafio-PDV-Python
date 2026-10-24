
# Desafio Nivel 1 - PDV com Descontos
# Desenvolvedora: Isabel Conceicao Sousa
# Trilha: Desenvolvimento Backend
# GitHub: Isabel828

compras = []

print("=== PDV COM DESCONTOS ===")

while True:
    entrada_valor = input(
        "\nValor da compra (0 para encerrar): "
    ).strip().replace(",", ".")

    # Validacao do valor da compra
    if not entrada_valor.lstrip("-").replace(".", "", 1).isdigit():
        print("Aviso: digite um valor numerico valido.")
        continue

    valor_original = float(entrada_valor)

    if valor_original < 0:
        print("Aviso: o valor da compra nao pode ser negativo.")
        continue

    if valor_original == 0:
        break

    # Entrada e validacao da idade
    entrada_idade = input("Idade do cliente: ").strip()

    if not entrada_idade.lstrip("-").isdigit():
        print("Aviso: digite uma idade inteira valida.")
        continue

    idade = int(entrada_idade)

    if idade < 0:
        print("Aviso: a idade nao pode ser negativa.")
        continue

    # Calculo dos descontos progressivos
    valor_final = valor_original

    # Regra 1: 20% de desconto para idade >= 65
    if idade >= 65:
        valor_final = round(valor_final * 0.80, 2)

    # Regra 2: 10% extra se o valor for maior que 100
    if valor_final > 100:
        valor_final = round(valor_final * 0.90, 2)

    desconto = round(valor_original - valor_final, 2)

    # Registro da compra no historico
    compras.append({
        "valor_original": valor_original,
        "idade": idade,
        "desconto": desconto,
        "valor_final": valor_final
    })

    print(f"Valor final: R$ {valor_final:.2f}")

# Calculo do resumo financeiro
total_bruto = 0
total_descontos = 0
total_final = 0

for compra in compras:
    total_bruto += compra["valor_original"]
    total_descontos += compra["desconto"]
    total_final += compra["valor_final"]

# Exibicao do resumo do dia
print("\n=== RESUMO DO DIA ===")
print(f"Quantidade de compras: {len(compras)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")

