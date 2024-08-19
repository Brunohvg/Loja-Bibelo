import flet as ft 
def _top():
    return ft.Container(
        bgcolor=ft.colors.RED,
        border_radius=20,
        width=335,
        height=80,  # Altura reduzida para ajustar o layout
        padding=ft.padding.only(top=5, left=8, right=8),
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        # Nome da loja
                        ft.Text(
                            value="Loja Bibelô",
                            size=18,
                            weight='bold',
                            color=ft.colors.WHITE,
                        ),
                        # Ícone do carrinho de compras
                        ft.IconButton(
                            icon=ft.icons.SPLITSCREEN,
                            icon_size=25,
                            icon_color=ft.colors.WHITE,
                            tooltip="Carrinho",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                # Menu de navegação
                ft.Row(
                    controls=[
                        ft.TextButton(
                            text="Calculadora",
                            style=ft.ButtonStyle(
                                color=ft.colors.WHITE,
                                padding=ft.padding.symmetric(horizontal=10)
                            )
                        ),
                        ft.TextButton(
                            text="Link",
                            style=ft.ButtonStyle(
                                color=ft.colors.WHITE,
                                padding=ft.padding.symmetric(horizontal=10)
                            )
                        ),
                        ft.TextButton(
                            text="Perfil",
                            style=ft.ButtonStyle(
                                color=ft.colors.WHITE,
                                padding=ft.padding.symmetric(horizontal=10)
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20  # Espaçamento entre os botões
                )
            ],
            spacing=10  # Espaçamento entre os elementos
        )
    )


def _session1():
    # Função que será chamada ao clicar no botão
    def calcular_frete(e):
        cep = cep_input.value
        peso = peso_input.value
        altura = altura_input.value
        largura = largura_input.value
        comprimento = comprimento_input.value

        # Validação: Verificar se todos os campos foram preenchidos
        if not cep or not peso or not altura or not largura or not comprimento:
            resultado_text.value = "Por favor, preencha todos os campos!"
            resultado_text.color = ft.colors.RED  # Muda a cor do texto para vermelho para indicar erro
        else:
            # Atualizar o widget de resultado com os dados
            resultado_text.value = (
                f"CEP: {cep}\n"
                f"Peso: {peso} kg\n"
                f"Altura: {altura} cm\n"
                f"Largura: {largura} cm\n"
                f"Comprimento: {comprimento} cm"
            )
            resultado_text.color = ft.colors.BLACK  # Volta a cor do texto para preto para exibir os dados corretamente
        
        # Atualizar o texto na interface
        resultado_text.update()

    # Campos de entrada
    cep_input = ft.TextField(
        hint_text='Digite o cep de destino ?',
        width=335,
        height=40,
        border_radius=40,
        prefix_icon=ft.icons.MAP,
        keyboard_type=ft.KeyboardType.NUMBER,
        text_vertical_align=1,
    )

    peso_input = ft.TextField(
        hint_text='Peso',
        width=70,
        height=40,
        border_radius=40,
        keyboard_type=ft.KeyboardType.NUMBER,
        text_vertical_align=1,
    )

    altura_input = ft.TextField(
        hint_text='A',
        width=70,
        height=40,
        border_radius=40,
        keyboard_type=ft.KeyboardType.NUMBER,
        text_vertical_align=1,
    )

    largura_input = ft.TextField(
        hint_text='L',
        width=70,
        height=40,
        border_radius=40,
        keyboard_type=ft.KeyboardType.NUMBER,
        text_vertical_align=1,
    )

    comprimento_input = ft.TextField(
        hint_text='C',
        width=70,
        height=40,
        border_radius=40,
        keyboard_type=ft.KeyboardType.NUMBER,
        text_vertical_align=1,
    )

    # Widget de texto para exibir o resultado ou mensagens de erro
    resultado_text = ft.Text(
        value="",
        size=16,
        color=ft.colors.BLACK
    )

    return ft.Container(
        bgcolor=ft.colors.WHITE,
        border_radius=20,
        width=335,
        height=900 * 0.35,
        padding=ft.padding.only(top=5, left=8, right=8),
        content=ft.Column([
            ft.Text(
                value='Calculador de frete',
                weight='bold',
                size=20,
            ),
            cep_input,
            ft.Row([
                peso_input,
                altura_input,
                largura_input,
                comprimento_input,
            ], alignment='center'),
            ft.ElevatedButton(
                text='Calcular',
                color=ft.colors.WHITE,
                bgcolor=ft.colors.GREEN,
                width=335,
                height=40,
                on_click=calcular_frete  # Aciona a função ao clicar
            ),
            resultado_text  # Mostra o resultado ou a mensagem de erro
        ], spacing=10)
    )
