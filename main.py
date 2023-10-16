# Pokedex Main Page

# Fleet modules
import flet as ft
from flet import border, colors

# Tools modules
from tools.screen_adapter import adapt_size as size
from tools import shapes

import aiohttp
import asyncio

from typing import Dict

WIDTH = size(720)
HEIGHT = size(1280)
RADIANTS = 3.14159

current_pokemon = 0

async def main(page: ft.Page):
    # TODO Constant for windows
    

    # TODO Prepare container
    page.window_width = WIDTH
    page.window_height = HEIGHT
    page.window_resizable = False
    page.padding = 0
    page.fonts = {
        "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.8/zpix.ttf"
    }
    page.theme = ft.Theme(font_family="zpix")
    
    #* Events
    async def query(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
            
    async def event_get_pokemon(e: ft.ContainerTapEvent):
        response: Dict
        global current_pokemon
        current_pokemon += 1 if e.control == arrow_up else -1
        number = (current_pokemon % 150) + 1
        print(number)
        url = f"https://pokeapi.co/api/v2/pokemon/{number}"
        response = await query(url)
        data = f"Name: {response.get('name')}\n\nAbilities:"
        for element in response.get('abilities'):
            ability = element.get('ability').get('name')
            data += f"\n{ability}"
        data += f"\n\nHeight: {response.get('height')}"
        text.value = data
        sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png"
        image.src = sprite_url
        await page.update_async()
        
    async def blink():
        while True:
            await asyncio.sleep(1)
            blue_ligth.bgcolor = colors.BLUE_100
            await page.update_async()
            await asyncio.sleep(0.1)
            blue_ligth.bgcolor = colors.BLUE
            await page.update_async()
            
            
    
    #* Upper content
    blue_ligth = ft.Container(
        width=size(66), 
        height=size(66),
        left=size(8),
        top=size(8),
        border_radius=size(50),
        bgcolor=colors.BLUE
    )
    blue_button = ft.Stack([
        ft.Container(
            width=size(80), 
            height=size(80),
            bgcolor=colors.WHITE,
            border_radius=size(50)
        ),
        blue_ligth
        
    ])
    items_upper = [
        ft.Container(blue_button, width=size(80), height=size(80)),
        ft.Container(width=size(40), height=size(40), bgcolor=colors.RED_200, border_radius=50),
        ft.Container(width=size(40), height=size(40), bgcolor=colors.YELLOW, border_radius=50),
        ft.Container(width=size(40), height=size(40), bgcolor=colors.GREEN, border_radius=50),
    ]
    
    #* Center content
    sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png"
    image = ft.Image(
        src=sprite_url,
        scale=10,
        width=size(30),
        height=size(30),
        top=(size(400) - size(50)) / 2,
        left=(size(600) - size(50)) / 2
    )
    stack_central = ft.Stack([
        ft.Container(width=size(600), height=size(400), bgcolor=colors.WHITE, border_radius=size(20)),
        ft.Container(width=size(550), height=size(350), bgcolor=colors.BLACK, top=size(25), left=size(25)),
        image
    ])
    
    #* Down content
    triangle = shapes.triangle()
    arrow_up = ft.Container(
        triangle, 
        width=size(80), 
        height=size(50), 
        on_click=event_get_pokemon
    )
    arrow_down = ft.Container(
        triangle, 
        rotate=ft.Rotate(angle=RADIANTS), 
        width=size(80), 
        height=size(50), 
        on_click=event_get_pokemon
    )
    arrows = ft.Column([
        arrow_up,
        arrow_down
    ])
    text = ft.Text(
        value='...',
        color=colors.BLACK,
        size=size(25)
    )
    
    items_down = [
        ft.Container(width=size(30)), #Left margin
        ft.Container(
            text, 
            padding=size(10), 
            width=size(400), 
            height=size(300), 
            bgcolor=colors.GREEN, 
            border_radius=size(20)
        ),
        ft.Container(width=size(30)), # Right Margin
        ft.Container(arrows, width=size(80), height=size(120)),
    ]
    
    #* Containers zone
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
        content=ft.Row(items_down),
        width=size(600),
        height=size(400),
        margin=ft.margin.only(top=size(40)),
    )
    
    # TODO Contanier
    columns = ft.Column(spacing=0, controls=[upper, center, down])
    container = ft.Container(
        columns,
        width=WIDTH,
        height=HEIGHT,
        bgcolor=colors.RED,
        alignment=ft.alignment.center,
    )
    await page.add_async(container)
    await blink()


if __name__ == "__main__":
    ft.app(target=main)
