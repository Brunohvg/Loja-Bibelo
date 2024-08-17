import flet as ft
from controls import _top
def main(page:ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.window_maximized = True
    
    Main = ft.Container(
        width=350,
        height=620,
        bgcolor=ft.colors.BLACK,
        border_radius=20,
        content=ft.Column(
            controls=[
                ft.Container(
                    width=335,
                    height=600,
                    bgcolor=ft.colors.WHITE38,
                    border_radius=20,
                    
                    content=ft.Stack(
                        controls=[
                            _top(),
                        ]
                    )
                )

            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.add(Main)

if __name__ =='__main__':
    ft.app(target=main, assets_dir='assets')