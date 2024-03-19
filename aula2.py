""" TextField, error_text, page.clean() """

from tkinter.font import BOLD
import flet as ft

def main(page: ft.Page):
    
    
    def login(event):
        if not entry_name.value and entry_pswd.value:
            entry_name.error_text = "All the fields need to be writed"
            page.update()
        elif not entry_pswd.value and entry_name.value:
            entry_pswd.error_text = "All the fields need to be writed"
            page.update()
        else:
            page.clean()
            name = entry_name.value
            pswd = entry_pswd.value
            print(f'Nome: {name}\nSenha: {pswd}')
            
            welcome = ft.Text(f'Welcome {name}', color="GREEN", weight=BOLD, size=30)
            page.add(welcome)
            page.update()
    
    entry_name = ft.TextField(label="name")
    entry_pswd = ft.TextField(label="password")
    login_button = ft.ElevatedButton("Login", on_click=login)
    
    page.add(
        entry_name,
        entry_pswd,
        login_button
    )
    
    
ft.app(target=main)