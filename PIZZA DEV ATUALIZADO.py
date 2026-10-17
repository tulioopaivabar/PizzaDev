import flet as ft
def main(page: ft.Page):


    page.title = "PizzaDev"
    page.padding = 20
    page.bgcolor = "#FCFDE4"
    largura= 300


    pedidos = []


    # Título
    titulo = ft.Container(
        width= 10000,
        height= 100,   
        padding=15,   
        bgcolor = "#BD0000",
        content = ft.Text("PizzaDev", color = "#FFFFFF", size=50, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER) )


    # Campos de entrada
    nome = ft.TextField(label="Nome do cliente",width=largura)

    sabor = ft.Dropdown(
        bgcolor= "#FCFDE4EC",
        label="Escolha o sabor",
        options=[
            ft.DropdownOption(key="Calabresa"),
            ft.DropdownOption(key="Frango"),
            ft.DropdownOption(key="Carne")
        ],width=largura
    )


    tamanho = ft.Dropdown(
        bgcolor= "#FCFDE4EC",
        label="Tamanho da pizza",
        options=[
            ft.DropdownOption(key="PEQUENA"),
            ft.DropdownOption(key="MÉDIA"),
            ft.DropdownOption(key="GRANDE")
        ],width=largura
    )


    quantidade = ft.TextField(
        label="Quantidade",
        keyboard_type=ft.KeyboardType.NUMBER,width=largura
    )


    observacao = ft.TextField(label="Observações", width=largura)


    # Campos de saída
    resultado = ft.Text("Nenhuma pizza adicionada!")
    vtotal = ft.Text("TOTAL: R$ 0,00", size=20)
    qtotal = ft.Text("QUANTIDADE: 0", size=20)
    lista_pedidos = ft.Column(
        controls=[]
    )


    # Função para adicionar o pedido
    def adicionar(e):
        if not nome.value or not sabor.value or not tamanho.value:
            resultado.value = "Preencha os dados do pedido."
        elif not quantidade.value or not quantidade.value.isdigit() or int(quantidade.value) <=0:
            resultado.value = "Informe uma quantidade válida."
        else:   
            valor_tamanho = 0


            if tamanho.value == "PEQUENA":
                valor_tamanho = 30 
            elif tamanho.value == "MÉDIA":
                valor_tamanho = 40
            else:
                valor_tamanho = 50


            pizza = {
                "Sabor": sabor.value,
                "Tamanho": tamanho.value,
                "Quantidade": int(quantidade.value),
                "Observacao": observacao.value or "Sem observações",
                "Subtotal" : int(quantidade.value)* valor_tamanho
            }


            pedidos.append(pizza)


            texto_pizza = (
                f"Pizza {len(pedidos)}\n"
                f"Sabor: {pizza['Sabor']}\n"
                f"Tamanho: {pizza['Tamanho']}\n"
                f"Quantidade: {pizza['Quantidade']}\n"
                f"Observação: {pizza['Observacao']}\n"
                f"Subtotal: {pizza['Subtotal']:.2f}\n"
            )
        
            lista_pedidos.controls.append(
                ft.Text(texto_pizza)
            )


            resultado.value = (
                f"{nome.value}, SUA PIZZA FOI ADICIONADA AO CARRINHO!"
            )


            #def limpar falsa
            sabor.value = None
            tamanho.value = None
            quantidade.value = ""
            observacao.value = ""


        valor_total = 0
        for i in pedidos:
            valor_total += i["Subtotal"]
        vtotal.value = f"TOTAL: R${valor_total:.2f}"


        quantidade_total = 0
        for i in pedidos:
            quantidade_total += i["Quantidade"]
        qtotal.value = f"QUANTIDADE: {quantidade_total}" 
            


        page.update()


    # Função para limpar os campos
    def limpar(e):


        nome.value = ""
        sabor.value = None
        tamanho.value = None
        quantidade.value = ""
        observacao.value = ""


        pedidos.clear()
        lista_pedidos.controls.clear()
        resultado.value = "Nenhuma pizza adicionada!"
        vtotal.value ="TOTAL: R$ 0,00"
        qtotal.value ="QUANTIDADE: 0"


        page.update()


    # Botões
    botao_adicionar = ft.Button(content="Adicionar", on_click=adicionar, width=largura / 2 - 5)
    botao_limpar = ft.Button(content="Limpar",color= "#BD0000", on_click=limpar, width=largura / 2 - 5)


    
    # Organização da interface
    coluna = ft.Column(
        controls=[
            titulo,
            nome,
            sabor,
            tamanho,
            quantidade,
            observacao,
            ft.Row(
                controls=[
                    botao_adicionar,
                    botao_limpar
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ), ft.Text(nome.value),
            resultado,
            lista_pedidos,
            ft.Row(controls=[qtotal, vtotal],
                   alignment=ft.MainAxisAlignment.CENTER)
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )


    page.add(coluna)    


ft.run(main)