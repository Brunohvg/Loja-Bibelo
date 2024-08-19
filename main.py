import flet as ft
from controls import _top, _session1

def main(page: ft.Page):
    # Configurações gerais da página para a web
    page.title = "Loja Bibelô"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK  # Definir cor de fundo da página

    # Container principal com ajustes de tamanho e estilo
    main_container = ft.Container(
        width=380,
        height=620,
        bgcolor=ft.colors.BLACK,
        border_radius=20,
        padding=ft.padding.all(10),
        content=ft.Container(
            width=335,
            height=600,
            bgcolor=ft.colors.WHITE,
            border_radius=20,
            padding=ft.padding.all(10),
            content=ft.Column(
                controls=[
                    _top(),      # Cabeçalho do aplicativo (ex. Loja Bibelô, ícone de carrinho)
                    _session1(), # Conteúdo principal (calculador de frete)
                ],
                spacing=20,  # Espaçamento entre o cabeçalho e o conteúdo
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
        ),
    )

    # Adiciona o container principal à página
    page.add(main_container)

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, assets_dir='assets')  # Executa como app web
