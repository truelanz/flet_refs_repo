
""" Configurações de Pagina """

import flet as ft

def main(page: ft.Page):
    
    # Titulo do app (page)
    page.title = " TESTE" 

    # Color Tema - DARK, SYSTEM or WHITE
    page.theme_mode = ft.ThemeMode.SYSTEM
    
      
    page.update()
ft.app(target=main, view=ft.WEB_BROWSER, port=8888)

