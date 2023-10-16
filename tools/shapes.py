import flet as ft
from tools.screen_adapter import adapt_size as size


def triangle():
    triangle_form = ft.canvas.Canvas(
        [
            ft.canvas.Path(
                [
                    ft.canvas.Path.MoveTo(size(40), size(0)),
                    ft.canvas.Path.LineTo(size(0), size(50)),
                    ft.canvas.Path.LineTo(size(80), size(50)),
                ],
                paint=ft.Paint(style=ft.PaintingStyle.FILL),
            )
        ],
        width=size(80),
        height=size(50),
    )
    return triangle_form
