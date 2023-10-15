# Pokedex Main Page

# Fleet modules
import flet as ft

# Tools modules
from tools.screen_adapter import adapt_size as size

async def main(page: ft.Page):
    # TODO Constant for windows
    WIDTH = size(720)
    HEIGHT = size(1280)

    # TODO Prepare container
    page.window_width = WIDTH
    page.window_height = HEIGHT
    page.window_resizable = False
    page.padding = 0
    
    items_upper = (
        ft.Container(width=size(80), height=size(80), border=ft.border.all()),
        ft.Container(width=size(40), height=size(40), border=ft.border.all()),
        ft.Container(width=size(40), height=size(40), border=ft.border.all()),
        ft.Container(width=size(40), height=size(40), border=ft.border.all()),
    )
    upper = ft.Container(
        content=ft.Row(items_upper),
        width=600 / 2,
        height=80 / 2,
        margin=ft.margin.only(top=size(40)),
        border=ft.border.all(),
    )
    center = ft.Container(
        width=600 / 2,
        height=400 / 2,
        margin=ft.margin.only(top=size(10)),
        border=ft.border.all(),
    )
    down = ft.Container(
        width=600 / 2,
        height=400 / 2,
        margin=ft.margin.only(top=size(40)),
        border=ft.border.all(),
    )
    columns = ft.Column(spacing=0, controls=[upper, center, down])
    # TODO Contanier
    container = ft.Container(
        columns,
        width=WIDTH,
        height=HEIGHT,
        bgcolor=ft.colors.RED,
        alignment=ft.alignment.center,
    )
    await page.add_async(container)


if __name__ == "__main__":
    ft.app(target=main)
