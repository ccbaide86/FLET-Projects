import flet as ft

def main(page: ft.Page):
    page.title = "Diagrama de bloques"
    
    # Crear los componentes de UI
    pll = ft.Container(
        content=ft.Text("PLL"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8,
        alignment=ft.alignment.center,
    )
    
    formatter_in = ft.Container(
        content=ft.Text("Formatter 64x32 FIFO Clipper"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=24
    )
    
    command_port_interface = ft.Container(
        content=ft.Text("Command Port Interface"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=24
    )
    
    decoder = ft.Container(
        content=ft.Text("Decoder"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8
    )
    
    sram_controller = ft.Container(
        content=ft.Text("SRAM Controller"),
        border=ft.border.all(1, ft.colors.BLACK),
        width=750,
        padding=8,
        alignment=ft.alignment.center,
    )
    
    clipper = ft.Container(
        content=ft.Text("Clipper"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8,
        width=100,
    )
    
    scaler_rotator = ft.Container(
        content=ft.Text("Scaler|Rotator"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8,
    )
    
    palette = ft.Container(
        content=ft.Text("Palette"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8
    )
    
    padding = ft.Container(
        content=ft.Text("Padding"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8
    )
    
    encoder = ft.Container(
        content=ft.Text("Encoder"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8
    )
    
    formatter_out = ft.Container(
        content=ft.Text("Formatter 64x32 FIFO"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=24
    )
    
    internal_sram = ft.Container(
        content=ft.Text("Internal SRAM (16KB)"),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8,
        alignment=ft.alignment.center,
    )
    
    led_on = ft.Container(
        bgcolor= ft.colors.BLACK,
        height=60,
        width=60,
        content=ft.Image(
            src='../assets/LED_ON.jpg',
            scale=ft.Scale('1')
        )
    )
    
    led_off = ft.Container(
        bgcolor= ft.colors.BLACK,
        height=60,
        width=60,
        content=ft.Image(
            src='../assets/LED_OFF.png',
            scale=ft.Scale('1')
        )
    )
    
    empty_container = ft.Container(
        content=ft.Text(""),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8,
        height=120,
        width=35,
        alignment=ft.alignment.center,
    )
    
    empty_container2 = ft.Container(
        content=ft.Text(""),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8,
        height=70,
        width=35,
        alignment=ft.alignment.center,
    )
    
    # Añadir componentes al layout
    page.add(
        ft.Column([
            ft.Row([
                ft.Container(width=200),
                sram_controller, 
                ft.Container(width=75),
                internal_sram,
            ]),
            ft.Row([
                ft.Container(width=800),
                clipper,
            ]),
            ft.Row([
                formatter_in,
                led_on,
                ft.Container(width=100),
                decoder,
                ft.Container(width=290),
                scaler_rotator,
                palette,
            ]),
            ft.Row([
                ft.Container(width=920),
                padding,
            ]), 
            ft.Row([
                pll,
                ft.Container(width=450),
                encoder,
                empty_container,
                led_on,
                ft.Container(width=300),
                empty_container2,
                formatter_out
            ]),
            command_port_interface,
        ])
    )
    

ft.app(target=main)

