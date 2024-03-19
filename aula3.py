""" Captuando teclas pressionadas pelo usuario (atalhos do teclado)  """

import flet as ft

def main(page: ft.Page):
    
    def tecla(event: ft.KeyboardEvent):
        page.add(
            ft.Text(f"Tecla precionada: {event.key}, Shift: {event.shift}, Control: {event.ctrl}, Alt: {event.alt}, Meta: {event.meta}")
        )
     
    page.on_keyboard_event = tecla 
    page.add(ft.Text('Pressione qualquer tecla, ou uma combinação de teclas: '))

ft.app(target=main)