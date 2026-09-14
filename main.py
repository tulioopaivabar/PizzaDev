pizzas = ["CALABRESA", "MARGUERITA", "FRANGO"]
precos = [40.0, 38.0, 42,0]

print ("======PIZZADEV======")
print ("CARDÁPIO")

for indice in range (len(pizzas)):
    print(f"{indice + 1} - {pizzas[indice]} : R$ {precos[indice]:2f}")
