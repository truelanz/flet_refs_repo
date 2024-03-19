""" Flet Hello World """

from tkinter.font import BOLD
import flet as ft

def main(page: ft.Page):
    hl = ft.Text("Hello World", size=100, weight=BOLD, color="red", bgcolor="white", rotate=0)
    page.controls.append(hl)

ft.app(target=main)