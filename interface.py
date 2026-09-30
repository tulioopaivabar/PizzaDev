import flet as ft 

def main(page: ft.Page): 
    page.title = "PizzaDev" 
    page.bgcolor = "#FCFDE4"

# TEXTO INICIAL DA PÁGINA
    titulo = ft.Container(
        width= 10000,
        height= 100,   
        padding=15,   
        bgcolor = "#BD0000",
        content = ft.Text("PizzaDev", color = "#FFFFFF", size=50, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER) )
    subtitulo = ft.Text("SABOR INCONFUNDÍVEL E TRADIÇÃO DESDE 1966", weight=ft.FontWeight.BOLD,)
    mensagemfunc = ft.Text("Funcionário, mantenha sempre o sorriso ao atender")  
    nome_aluno = ft.Text("Túlio Paiva Barreto")

# SELEÇÃO DE QUANTIDADE DE PIZZAS
    mensagem = ft.Text("Selecione o sabor: ")
    quantidade = ft.TextField(label = "DIGITE A QUANTIDADE", value = "1")
    tamanho = ft.RadioGroup(
        content = ft.Row([ft.Radio(value = "M", label = "M"),
                          ft.Radio(value = "G", label = "G")]),
    value = "M")
    resultado = ft.Text("VALOR PARCIAL:[         ] ")

    def calcular(e):
        estado["tamanho"] = tamanho.value

        if not quantidade.value.isdigit():
            resultado.value = "Digite uma quantidade inteira."
            return
        qtd = int(quantidade.value)
        if qtd < 1 or qtd > 10:
            resultado.value = "Quantidade deve ser entre 1 e 10."
            return
        preco = 32 if tamanho.value == "M" else 42
        resultado.value = f"Valor parcial: R$: {preco * qtd:.2f}"

        estado["quantidade"] = int(quantidade.value)
        page.update()

# SABORES DISPONIVEIS DE PIZZA

    PIZZAS = [{"id":"P01", "nome":"CALABRESA", "m":32, "g":42},
              {"id":"P02", "nome":"MUSSARELA", "m":32, "g":42},
              {"id":"P03", "nome":"FRANGO", "m":32, "g":42},
              {"id":"P04", "nome":"PORTUGUESA", "m":32, "g":42}]

# FUNÇÃO PARA CRIAÇÃO DOS CARDS DO CARDÁPIO 
    def criar_card(pizza):
        def selecionar(e):
            estado["pizza"] = pizza
            mensagem.value = f"Selecionada: {pizza['nome']}"
            page.update()

        return ft.Container(
            width=600,
            height=300,
            padding=15,
            border_radius=30,
            bgcolor=ft.Colors.WHITE,
            on_click=selecionar,
            content=ft.Column([
                ft.Text(pizza["nome"], size=20),
                ft.Text(f'M: R$ {pizza["m"]} | G: R$ {pizza["g"]}')
            ])
        )
    
    cardapio = ft.Row(
        controls = [criar_card(p) for p in PIZZAS],
        wrap = True,
        spacing = 20,
        run_spacing = 20)

# não sei
    
    estado = {"pizza": None, "tamanho": "M", "quantidade": 1}
    area = ft.Container(expand=True)

    def mostrar_inicio():
        area.content = ft.Column([
            ft.Text("PizzaDev", size=30),
            ft.Button("Abrir cardápio", on_click=lambda e: mostrar_cardapio())
        ])
        page.update()

    mostrar_inicio()

    
    def mostrar_cardapio():
        area.content = ft.Column([
            ft.Text("Cardápio"),
            mensagem,
            cardapio,
            quantidade, 
            tamanho,
            ft.Button("CALCULAR", on_click = calcular),
            resultado,
            ft.Button("Voltar", on_click=lambda e: mostrar_inicio())
        ])
        page.update()

    obs = ft.Text("AGUARDANDO. . .", size = 12, color = "#FF0000", )
            
    page.add(
        ft.Column(
            controls=[titulo, subtitulo, mensagemfunc, nome_aluno, area, obs],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
    )
    
ft.run(main) 
