
"""  Lista de itens unsado GRIDVIEW com CONTAINER e os.environ """

import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000" # Para a aplicação conseguir ler muitos itens.

def main(page: ft.Page):
    
    linha = ft.Row(wrap=True, scroll="always", expand=True) # wrap (quebrar linha), scroll
    page.add(linha)
    
    for i in range(99):
        linha.controls.append(
            ft.Container(
                ft.Text(f'Item {i}'),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_600,
                border=ft.border.all(2, ft.colors.BLUE_50),
                border_radius=ft.border_radius.all(5)
            )
        )
    
    page.update()
ft.app(target=main)