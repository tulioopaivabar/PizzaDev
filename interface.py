import flet as ft 

def main(page: ft.Page): 
    page.title = "PizzaDev" 
    titulo = ft.Text("PizzaDev", size=32, weight=ft.FontWeight.BOLD) 
    subtitulo = ft.Text("Funcionário, mantenha sempre o srriso ao atender") 
    aluno = ft.Text("Túlio Paiva Barreto")
    obs = ft.Text("AGUARDANDO. . .")
    page.add(titulo, subtitulo, aluno, obs) 
ft.run(main) 
