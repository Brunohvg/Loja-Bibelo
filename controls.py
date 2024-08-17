import flet as ft 
def _top():
    top = ft.Container(
        bgcolor=ft.colors.RED,
        border_radius=20,
        width=335,
        height=600 * 0.35,
        padding=ft.padding.only(top=5, left=8, right=8),
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            value="Loja Bibelô",
                            size=13,
                            weight='bold',
                            color=ft.colors.WHITE,
                        ),
                        ft.Row(
                            controls=[
                                ft.Stack(
                                    controls=[
                                        ft.IconButton(
                                            icon_size=25,
                                            icon=ft.icons.SHOPPING_CART_CHECKOUT,
                                            icon_color=ft.colors.WHITE,
                                            
                                        )
                                    ]
                                    
                                )
                            ]
                            
                        )
                    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    
                )
            ]
        )
    )
    return top
