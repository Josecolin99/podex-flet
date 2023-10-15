# Pokedex Main Page

# Fleet modules
import flet as ft
from flet import border, colors

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
    
    #* Upper content
    blue_button = ft.Stack([
        ft.Container(
            width=size(80), 
            height=size(80),
            bgcolor=colors.WHITE,
            border_radius=size(50)
        ),
        ft.Container(
            width=size(66), 
            height=size(66),
            left=size(8),
            top=size(8),
            bgcolor=colors.BLUE,
            border_radius=size(50)
        )
    ])
    items_upper = (
        ft.Container(blue_button, width=size(80), height=size(80)),
        ft.Container(width=size(40), height=size(40), bgcolor=colors.RED_200, border_radius=50),
        ft.Container(width=size(40), height=size(40), bgcolor=colors.YELLOW, border_radius=50),
        ft.Container(width=size(40), height=size(40), bgcolor=colors.GREEN, border_radius=50),
    )
    
    #* Center content
    stack_central = ft.Stack([
        ft.Container(width=size(600), height=size(400), bgcolor=colors.WHITE),
        ft.Container(width=size(550), height=size(350), bgcolor=colors.BLACK, top=size(25), left=size(25)),
        ft.Image(
            src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/80.png",
            scale=10,
            width=size(50),
            height=size(50),
            top=(size(400) - size(50)) / 2,
            left=(size(600) - size(50)) / 2
        )

    ])
    
    #* Down content
    upper = ft.Container(
        content=ft.Row(items_upper),
        width=size(600),
        height=size(80),
        margin=ft.margin.only(top=size(40)),
    )
    center = ft.Container(
        content=stack_central,
        width= size(600),
        height=size(400),
        margin=ft.margin.only(top=size(20)),
        alignment=ft.alignment.center
    )
    down = ft.Container(
        width=size(600),
        height=size(400),
        margin=ft.margin.only(top=size(40)),
        border=border.all(),
    )
    columns = ft.Column(spacing=0, controls=[upper, center, down])
    # TODO Contanier
    container = ft.Container(
        columns,
        width=WIDTH,
        height=HEIGHT,
        bgcolor=colors.RED,
        alignment=ft.alignment.center,
    )
    await page.add_async(container)


if __name__ == "__main__":
    ft.app(target=main)
