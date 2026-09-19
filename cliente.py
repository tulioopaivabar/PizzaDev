cliente = {}
while True:
    nome = input("DIGITE O SEU NOME: ").strip()
    if not nome:
        print("O CAMPO NÃO PODE ESTAR VAZIO")
    else:
        break
    telefone = input("DIGITE SEU TELEFONE: ")
    cliente[nome] = telefone

    print(cliente)