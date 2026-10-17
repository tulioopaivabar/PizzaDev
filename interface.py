import flet as ft 


def main(page: ft.Page): 
    page.title = "PizzaDev" 
    page.bgcolor = "#FCFDE4"

    largura = 600
    valor_tamanho = 0
    pedidos = []

#-----------------------------
#        PÁGINA PIZZA
#-----------------------------
    # *Função de cálculo
    area_pizza = ft.Container(expand=True)
    mensagem = ft.Text("SELECIONE O SABOR: ", size = 30, text_align=ft.TextAlign.CENTER)
    sabor = ""
    quantidade = ft.TextField(label = "DIGITE A QUANTIDADE", keyboard_type=ft.KeyboardType.NUMBER, value = "1")
    tamanho = ft.RadioGroup(
        content = ft.Row([ft.Radio(value = "P", label = "P | R$:26"), ft.Radio(value = "M", label = "M | R$:32"), ft.Radio(value = "G", label = "G | R$:42")]), value = "P")
    resultado = ft.Text("VALOR PARCIAL:[         ] ")
    calculo = False
    lista_pedidos = ft.Column(
        controls=[])

    def calcular(e):
        if not quantidade.value:
            resultado.value = "PREENCHA TODOS OS CAMPOS"
            return 

        if not quantidade.value.isdigit():
            resultado.value = " QUANTIDADE INVÁLIDA!"
            return
        
        if int(quantidade.value) < 1 or int(quantidade.value) > 10:
            resultado.value = "QUANTIDADE DEVE SER ENTRE 1 E 10."
            return

        global valor_tamanho
        if tamanho.value == "P":
            valor_tamanho = 26
        elif tamanho.value == "M":
            valor_tamanho = 32 
        elif tamanho.value == "G":
            valor_tamanho = 42
        resultado.value = f"VALOR PARCIAL: R$: {valor_tamanho * int(quantidade.value):.2f}"

        global calculo
        calculo = True

        page.update()

    def limpar_selecao(e):
        global calculo
        tamanho.value = "P"
        quantidade.value = "1"
        observacao.value = ""
        resultado.value = "VALOR PARCIAL:[         ] "
        calculo = False
        page.update()

    def adicionar(e):
        global calculo
        if calculo == False:
            resultado.value = "REALIZE O CÁLCULO PARCIAL PRIMEIRO!"
            return
        elif calculo == True:
            global valor_tamanho
            item = {
                "Sabor": sabor,
                "Tamanho": tamanho.value,
                "Quantidade": int(quantidade.value),
                "Observacao": observacao.value or "Sem observações",
                "Subtotal" : int(quantidade.value)* valor_tamanho
            }

            pedidos.append(item)

            texto_pizza = (
                f"Pizza {len(pedidos)}\n"
                f"Sabor: {item['Sabor']}\n"
                f"Tamanho: {item['Tamanho']}\n"
                f"Quantidade: {item['Quantidade']}\n"
                f"Observação: {item['Observacao']}\n"
                f"Subtotal: {item['Subtotal']:.2f}\n"
            )
        
            lista_pedidos.controls.append(
                ft.Text(texto_pizza)
            )

            resultado.value = (
                f"{input_nome.value}, SUA PIZZA FOI ADICIONADA AO CARRINHO!"
            )

            #def limpar falsa
            tamanho.value = "P"
            quantidade.value = "1"
            observacao.value = ""
            resultado.value = "VALOR PARCIAL:[         ] "
            calculo = False

        page.update()

    observacao =ft.TextField(label = "OBSERVAÇÕES:")

    def mostrar_pizza(pizza):
        page.clean()
        global sabor 
        sabor = pizza["nome"]
        mensagem.value = f"SELECIONADA: {pizza['nome']}"
        area_pizza.content = ft.Column(controls=[
            ft.Container(
                width= 10000,
                height= 100,   
                padding=15,   
                bgcolor = "#BD0000",
                content = ft.Text("PizzaDev", color = "#FFFFFF", size=50, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)),
            mensagem,
            ft.Container(width=largura,
                        height=600,
                        padding=15,
                        border_radius=30,
                        bgcolor=ft.Colors.WHITE,
                        content=ft.Column([ft.Text("[FOTO]", size=80, text_align=ft.TextAlign.CENTER)])),
            ft.Container(width=largura,
                        height=150,
                        padding=15,
                        border_radius=30,
                        bgcolor=ft.Colors.WHITE,
                        content=ft.Column([ft.Text(pizza["nome"], size=25),
                                           ft.Text(pizza["ingredientes"], size = 20)])),
            ft.Container(width=largura,
                        height=100,
                        padding=15,
                        border_radius=30,
                        bgcolor=ft.Colors.WHITE,
                        content= observacao),
            ft.Row([quantidade, tamanho,]),
            resultado,
            ft.Row([ft.Button("CALCULAR", on_click = calcular, width = largura / 2 - 10),
                   ft.Button("LIMPAR", on_click = limpar_selecao, width = largura / 2 - 10)]),
            ft.Button("ADICIONAR", on_click = adicionar, width = largura), 
            lista_pedidos,
            ft.Button("VOLTAR", on_click=lambda e: mostrar_cardapio()),
        ])
        page.add(ft.Column( controls=[area_pizza,
                                    obs], 
                            scroll=ft.ScrollMode.AUTO, expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER,))
        area_pizza.update()
        page.update()


#-----------------------------
#      PÁGINA CARDÁPIO
#-----------------------------
    area_cardapio = ft.Container(expand=True)

    def mostrar_cardapio():
        if not input_nome.value:
                    obs.value="PREENCHA TODOS OS DADOS!"
        else:
            page.clean()
            obs.value = "AGUARDANDO. . ."
            area_cardapio.content = ft.Column(controls=[
                ft.Container(
                                width= 10000,
                                height= 100,   
                                padding=15,   
                                bgcolor = "#BD0000",
                                content = ft.Text("CARDÁPIO", color = "#FFFFFF", size=50, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)),
                ft.Container(
                                width= 400,
                                height= 50,   
                                padding=12,
                                border_radius=30, 
                                bgcolor = "#BD0000",
                                content = ft.Text(f"SEJA BEM, VINDO(A), {input_nome.value}!", color = "#FFFFFF", size=18, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)),
                cardapio,
                ft.Button("Voltar", on_click=lambda e: mostrar_inicio() )
            ])
            page.add(ft.Column( controls=[area_cardapio, 
                                        obs], 
                                scroll=ft.ScrollMode.AUTO, expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER))
            area_cardapio.update()
            page.update()

    #*Itens do cardápio
    PIZZAS = [{"id":"P01", "nome":"CALABRESA","p":26, "m":32, "g":42, "ingredientes": "Massa, molho de tomate, linguiça calabresa fatiada, cebola, queijo mussarela e orégano."},
              {"id":"P02", "nome":"MUSSARELA","p":26, "m":32, "g":42, "ingredientes": "Massa, molho de tomate, queijo mussarela."},
              {"id":"P03", "nome":"FRANGO","p":26, "m":32, "g":42, "ingredientes": "Massa, molho de tomate, queijo mussarela, frango desfiado."},
              {"id":"P04", "nome":"PORTUGUESA","p":26, "m":32, "g":42, "ingredientes": "Massa, molho de tomate, queijo mussarela, presunto, ovos cozidos, cebola, tomate e azeitonas."}]
    
    #*Função para criação e adição de itens em card ao cardápio
    def criar_card(pizza):

        return ft.Container(
            width=largura,
            height=300,
            padding=15,
            border_radius=30,
            bgcolor=ft.Colors.WHITE,
            on_click=lambda e: mostrar_pizza(pizza),
            content=ft.Column([
                ft.Text(pizza["nome"], size=20),
                ft.Text(pizza["ingredientes"]), 
                ft.Text(f'P: R$ {pizza["p"]} | M: R$ {pizza["m"]} | G: R$ {pizza["g"]}')])
        )

    
    cardapio = ft.Row(
        controls = [criar_card(p) for p in PIZZAS],
        wrap = True,
        spacing = 20,
        run_spacing = 20)


#-----------------------------
#        PÁGINA INCIAL
#-----------------------------
    
    titulo = ft.Container(
        width= 10000,
        height= 100,   
        padding=15,   
        bgcolor = "#BD0000",
        content = ft.Text("PizzaDev", color = "#FFFFFF", size=50, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER) )
    subtitulo = ft.Text("SABOR INCONFUNDÍVEL E TRADIÇÃO DESDE 1966", weight=ft.FontWeight.BOLD,)
    mensagemfunc = ft.Text("Funcionário, mantenha sempre o sorriso ao atender")  
    nome_aluno = ft.Text("TÚLIO PAIVA BARRETO")

    texto = ft.Column(controls= [titulo, subtitulo, mensagemfunc, nome_aluno])
 
    input_nome = ft.TextField(label="Nome do cliente:",width=200)

    obs = ft.Text("", size = 14, color = "#FF0000", )

    def mostrar_inicio():
        page.clean(),
        page.add(ft.Column( controls=[texto, input_nome,
                                    area_cardapio, 
                                    obs],
                            scroll=ft.ScrollMode.AUTO, expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER)),
        area_cardapio.content = ft.Column([ft.Button("Abrir cardápio", on_click= lambda e: mostrar_cardapio())])
        page.update()
    mostrar_inicio()
ft.run(main) 