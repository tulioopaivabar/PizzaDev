import flet as ft 

def main(page: ft.Page): 
    page.title = "PizzaDev" 
    page.bgcolor = "#E74C3C"

    titulo = ft.Text("PizzaDev", size=32, weight=ft.FontWeight.BOLD) 
    subtitulo = ft.Text("SABOR INCONFUNDÍVEL E TRADIÇÃO DESDE 1966")
    mensagemfunc = ft.Text("Funcionário, mantenha sempre o sorriso ao atender")  
    nome_aluno = ft.Text("Túlio Paiva Barreto")
    obs = ft.Text("AGUARDANDO. . .", size = 12, color = "#FF0000")

    card1 = ft.Container(
        padding=15,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column([
            ft.Text("CALABRESA", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Calabresa, cebola e muçarela"),
            ft.Row([ft.Text("M: R$ 32"), ft.Text("G: R$ 42")])
        ])
    )

    card2 = ft.Container(
        padding=15,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column([
            ft.Text("MUSSARELA", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Mussarela, molho de tomate, orégano"),
            ft.Row([ft.Text("M: R$ 32"), ft.Text("G: R$ 42")])
        ])
    )

    card3 = ft.Container(
        padding=15,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column([
            ft.Text("FRANGO", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Frango, azeitona, mussarela, molho de tomate, orégano"),
            ft.Row([ft.Text("M: R$ 32"), ft.Text("G: R$ 42")])
        ])
    )

    card4 = ft.Container(
        padding=15,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column([
            ft.Text("PORTUGUESA", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Ovo cozido, presunto, cebola mussarela, molho de tomate, orégano"),
            ft.Row([ft.Text("M: R$ 32"), ft.Text("G: R$ 42")])
        ])
    )

    cardapio = ft.Row(
        controls = [card1, card2, card3, card4],
        wrap = True,
        spacing = 20,
        run_spacing = 20)

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


    page.add(titulo, subtitulo, mensagemfunc, nome_aluno, escolha, quantidade, mensagem, tamanho, resultado,
             ft.Button("CALCULAR", on_click = calcular), cardapio, obs) 

ft.run(main) 
