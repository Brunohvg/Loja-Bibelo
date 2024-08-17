import flet as ft 
def _top():
    top = ft.Container(
        bgcolor=ft.colors.RED,
        border_radius=20,
        width=335,
        height=600 * 0.35,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            value="Loja Bibelô",
                            size=20,
                            weight='bold',
                        )
                    ]
                )
            ]
        )
    )
    return top
