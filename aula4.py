"""  Lista de itens usando FOR (primeiro metodo) """

import flet as ft

def main(page: ft.Page):
    page.scroll = "always"
    
    for i in range(4,37,2):
        page.controls.append(ft.Text(f'Linha {i}'))
    page.update() 
    page.update() 
    
ft.app(target=main)