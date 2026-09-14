pizzas = ["CALABRESA", "MARGUERITA", "FRANGO"]
precos = [40.0, 38.0, 42,0]

print ("======PIZZADEV======")
print ("CARDÁPIO")

for indice in range (len(pizzas)):
    print(f"{indice + 1} - {pizzas[indice]} : R$ {precos[indice]:2f}")

opcao = input("ESCOLHA O NUMERO DA PIZZA: ")

if opcao.isdigit() and 1 <= int(opcao) <= len(pizzas):
    indice - int(opcao) - 1
    print (f"PIZZA ESCOLHIDA: {pizzas[indice]}")
    print(f"PREÇO UNITÁRIO: R$ {precos[indice]}:.2f")
else:
    print("OPCAO INVALIDA")