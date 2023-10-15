import flet as ft


async def main(page: ft.Page):
    # TODO Constant for windows
    WIDTH = 720 / 2
    HEIGHT = 1280 / 2

    # TODO Prepare container
    page.window_width = WIDTH
    page.window_height = HEIGHT
    page.window_resizable = False
    page.padding = 0
    
    items_upper = (
        ft.Container(width=80 / 2, height=80 / 2, border=ft.border.all()),
        ft.Container(width=40 / 2, height=40 / 2, border=ft.border.all()),
        ft.Container(width=40 / 2, height=40 / 2, border=ft.border.all()),
        ft.Container(width=40 / 2, height=40 / 2, border=ft.border.all()),
    )
    upper = ft.Container(
        content=ft.Row(items_upper),
        width=600 / 2,
        height=80 / 2,
        margin=ft.margin.only(top=40),
        border=ft.border.all(),
    )
    center = ft.Container(
        width=600 / 2,
        height=400 / 2,
        margin=ft.margin.only(top=10),
        border=ft.border.all(),
    )
    down = ft.Container(
        width=600 / 2,
        height=400 / 2,
        margin=ft.margin.only(top=40),
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
