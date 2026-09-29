import flet as ft 

def main(page: ft.Page): 
    page.title = "PizzaDev" 
    page.bgcolor = "#FCFDE4"

    titulo = ft.Container(
        width= 10000,
        height= 100,   
        padding=15,   
        bgcolor = "#BD0000",
        content = ft.Text("PizzaDev", color = "#FFFFFF", size=50, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER) )

    subtitulo = ft.Text("SABOR INCONFUNDÍVEL E TRADIÇÃO DESDE 1966", weight=ft.FontWeight.BOLD,)
    mensagemfunc = ft.Text("Funcionário, mantenha sempre o sorriso ao atender")  
    nome_aluno = ft.Text("Túlio Paiva Barreto")

    mensagem = ft.Text("Selecione o sabor: ")
    
    def escolher_calabresa(e):
        mensagem.value = "Selecionada: Calabresa"
        page.update()

    def escolher_mussarela(e):
        mensagem.value = "Selecionada: Mussarela"
        page.update()

    def escolher_frango(e):
        mensagem.value = "Selecionada: Frango"
        page.update()

    def escolher_portuguesa(e):
        mensagem.value = "Selecionada: Portuguesa"
        page.update()

    
    escolha = ft.Row(
        controls = [ft.Button("ESCOLHER CALABRESA", on_click = escolher_calabresa),
            ft.Button("ESCOLHER MUSSARELA", on_click = escolher_mussarela),
            ft.Button("ESCOLHER FRANGO", on_click = escolher_frango),
            ft.Button("ESCOLHER PORTUGUESA", on_click = escolher_portuguesa,)])

    quantidade = ft.TextField(label = "Quantidade", value = "1")

    tamanho = ft.RadioGroup(
        content = ft.Row([ft.Radio(value = "M", label = "M"),
                           ft.Radio(value = "G", label = "G")
    ]),
    value = "M")

    resultado = ft.Text()
    def calcular(e):
        if not quantidade.value.isdigit():
            resultado.value = "Digite uma quantidade inteira."
            return
        qtd = int(quantidade.value)
        if qtd < 1 or qtd > 10:
            resultado.value = "Quantidade deve ser entre 1 e 10."
            return
        preco = 32 if tamanho.value == "M" else 42
        resultado.value = f"Valor parcial: R$: {preco * qtd:.2f}"
        page.update

    PIZZAS = [{"id":"P01", "nome":"CALABRESA", "m":32, "g":42},
              {"id":"P02", "nome":"MUSSARELA", "m":32, "g":42},
              {"id":"P03", "nome":"FRANGO", "m":32, "g":42},
              {"id":"P04", "nome":"PORTUGUESA", "m":32, "g":42}]

    def criar_card(pizza):
        return ft.Container(
            width= 600,
            height= 300,
            padding=15,
            border_radius=30,
            bgcolor=ft.Colors.WHITE,
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

    obs = ft.Text("AGUARDANDO. . .", size = 12, color = "#FF0000", )
    
    page.add(titulo, subtitulo, mensagemfunc, nome_aluno, escolha, quantidade, mensagem, tamanho, resultado,
             ft.Button("CALCULAR", on_click = calcular), cardapio, obs) 

ft.run(main) 
