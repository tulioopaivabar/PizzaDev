while True:
    nome = input("DIGITE O SEU NOME: ").upper().strip()
    if nome and nome.replace(" ", "").isalpha():
        break
    print("O CAMPO NÃO PODE ESTAR VAZIO, E DEVE CONTER APENAS LETRAS!")
print("NOME CADASTRADO COM SUCESSO!")

while True:
    telefone = input("DIGITE O SEU TELEFONE: ").strip()
    if telefone.isdigit() and len(telefone) >= 11:
        break
    print("O TELEFONE DIGITADO É INVÁLIDO!")
print("TELEFONE CADASTRADO COM SUCESSO!")

print(f"NOME: {nome}\nTELEFONE: {telefone}")
