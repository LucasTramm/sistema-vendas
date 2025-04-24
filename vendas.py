vendas = []

while True:
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade vendida: "))
    preco = float(input("Preço unitário (R$): "))

    vendas.append({
        "produto": produto,
        "quantidade": quantidade,
        "preco": preco
    })

    cont = input("Deseja continuar? (s/n): ")
    if cont.lower() != 's':
        break

print("\n--- Vendas Realizadas ---")
for venda in vendas:
    total = venda["quantidade"] * venda["preco"]
    print(f"{venda['produto']} - {venda['quantidade']} unidades - Total: R$ {total:.2f}")