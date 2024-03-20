"""  Lista de itens usando LISTVIEW  """

import flet as ft

def main(page: ft.Page):
    page.scroll = "always"
    lista = ft.ListView(spacing=20)
    
    for i in range(100):
        lista.controls.append(ft.Text(f'lista {i}'))
        
    page.add(lista)
    page.update()
    
ft.app(target=main)