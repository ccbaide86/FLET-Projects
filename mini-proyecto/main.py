import flet as ft
import random
import paho.mqtt.client as mqtt

def main(page: ft.Page):
    page.title = "WorkCentre Pro 412 Simulation"
    page.theme_mode = ft.ThemeMode.DARK  

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
            scale=ft.Scale('1'),
            color=ft.colors.BLACK
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
        height=150,
        width=35,
        alignment=ft.alignment.center,
    )
    
    arrow_container = ft.Container(
        content=ft.Column([
            ft.Icon(name=ft.icons.SUBDIRECTORY_ARROW_RIGHT , color=ft.colors.WHITE, size=30), 
            ft.Icon(name=ft.icons.ARROW_FORWARD , color=ft.colors.WHITE, size=30), 
            ]),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
        height=120,
        width=35,
        alignment=ft.alignment.center,
    )
    
    arrow_container2 = ft.Container(
        content=ft.Column([
            ft.Icon(name=ft.icons.SUBDIRECTORY_ARROW_RIGHT , color=ft.colors.WHITE, size=30), 
            ft.Icon(name=ft.icons.ARROW_FORWARD , color=ft.colors.WHITE, size=30), 
            ]),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
        height=120,
        width=35,
        alignment=ft.alignment.center,
    )
    
    empty_container2 = ft.Container(
        content=ft.Text(""),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=8,
        height=75,
        width=35,
        alignment=ft.alignment.center,
    )
    
    compare = ft.Container(
        content=ft.Row([ft.Text("Address"), ft.Icon(name=ft.icons.COMPARE_ARROWS , color=ft.colors.WHITE, size=30), ft.Text('Data')]),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
        alignment=ft.alignment.center,
    )
    
    title = ft.Container(
        content=ft.Text("External Ram",  weight=ft.FontWeight.BOLD, size=16),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
        alignment=ft.alignment.center,
    )
    
    subtitle = ft.Container(
        content=ft.Row([ft.Text("Address"), 
                        ft.Icon(name=ft.icons.ARROW_UPWARD , color=ft.colors.WHITE, size=30), 
                        ft.Container(width=100),
                        ft.Icon(name=ft.icons.ARROW_DOWNWARD , color=ft.colors.WHITE, size=30),
                        ft.Text('Data')
                        ]),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
        alignment=ft.alignment.center,
    )
    
    Input_Data =  ft.Container(
        content=ft.Column([ft.Text("Input Data",  weight=ft.FontWeight.BOLD, size=15),
                        ft.Icon(name=ft.icons.ARROW_FORWARD , color=ft.colors.WHITE, size=30,)
                        ]),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
        alignment=ft.alignment.center,
    )
    
    CLOCK_IN =  ft.Container(
        content=ft.Column([ft.Text("Clock In",  weight=ft.FontWeight.BOLD, size=10),
                        ft.Icon(name=ft.icons.DOUBLE_ARROW , color=ft.colors.WHITE, size=20,)
                        ]),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
        alignment=ft.alignment.center,
    )
    
    System_Clock =  ft.Container(
        content=ft.Column([ft.Text("System Clock",  weight=ft.FontWeight.BOLD, size=10),
                        ft.Icon(name=ft.icons.DOUBLE_ARROW , color=ft.colors.WHITE, size=20,)
                        ]),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
        alignment=ft.alignment.center,
    )
    
    Control_Data =  ft.Container(
        content=ft.Column([ft.Text("Control Data",  weight=ft.FontWeight.BOLD, size=15),
                        ft.Icon(name=ft.icons.ARROW_FORWARD , color=ft.colors.WHITE, size=30,)
                        ]),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
        alignment=ft.alignment.center,
    )
    
    Output_Data =  ft.Container(
        content=ft.Column([ft.Text("Output Data",  weight=ft.FontWeight.BOLD, size=15),
                        ft.Icon(name=ft.icons.ARROW_FORWARD , color=ft.colors.WHITE, size=30,)
                        ]),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
        alignment=ft.alignment.center,
    )
    
    # Definir una lista de errores por componente
    errores = {
        "sram_controller": ["Error en SRAM Controller, Diagnostico: Reiniciar Dispositivo"],
        "internal_sram": ["Error en Internal SRAM (16KB), Diagnostico: Reiniciar Dispositivo"],
        "clipper": ["Error en Clipper, Cambiar Clipper"],
        "Input_Data": ["Error en Input Data, Diagnostico: Revise bien la Conexion"],
        "formatter_in": ["Error en Formatter 64x32 FIFO Clipper, Diagnostico: Cambie el Formatter"],
        "decoder": ["Fallo en el Decoder, Diagnostico: Cambiar el Decoder"],
        "scaler_rotator": ["Error en Scaler|Rotator, Diagnostico: Cambiar el Scalar Rotator"],
        "palette": ["Error en Palette, Diagnostico: Cambiar el Palette"],
        "padding": ["Error en Padding, Diagnostico: Cambiar el Padding"],
        "CLOCK_IN": ["Error en Clock In, Diagnostico: Reiniciar el Dispositivo"],
        "pll": ["Error en PLL, Diagnostico: Reinicar el Discpositivo"],
        "System_Clock": ["System Clock desconfigurado, Diagnostico: Reiniciar el Dispositivo"],
        "encoder": ["Error en Encoder, Diagnostico: Cambiar el Encoder"],
        "formatter_out": ["Error en Formatter 64x32 FIFO, Diagnostico: Cambiar el Formatter"],
        "Output_Data": ["Error en Output Data, Diagnostico: Revisar la Conexion"],
        "Control_Data": ["Error en Control Data, Diagnostico: Reiniciar el Dispositivo"],
        "command_port_interface": ["Error en Command Port Interface, Diagnostico: Revisar la Conexion"],
    }
    
    # Funciones de las LEDs y manejo de errores simulados
    led1_state = ft.Ref[ft.Container]()
    led2_state = ft.Ref[ft.Container]()
    
    # Crear un contenedor para mostrar mensajes de error
    error_message_container = ft.Ref[ft.Container]()
    
    def show_error_message():
        # Escoger un componente aleatorio del diccionario de errores
        componente = random.choice(list(errores.keys()))
        # Escoger un mensaje de error aleatorio para ese componente
        error_message = random.choice(errores[componente])
        error_message_container.current.content = ft.Text(error_message)
        error_message_container.current.visible = True
        error_message_container.current.update()

        broker = "test.mosquitto.org"
        port = 1883
        topic = "academics/IoT2"

        # Crear una nueva instancia del cliente MQTT
        client = mqtt.Client()

        # Conectar al broker
        client.connect(broker, port)

        # Publicar un mensaje para encender el LED
        response = client.publish(topic, error_message)

        # Desconectar del brokers
        client.disconnect()
    
    def hide_error_message(e):
        error_message_container.current.visible = False
        error_message_container.current.update()
    
    def toggle_leds(e):
        random_number1 = random.randint(0, 1)
        random_number2 = random.randint(0, 1)
        led_indicator = random_number1 + random_number2
        
        broker = "test.mosquitto.org"
        port = 1883
        topic = "academics/IoT"

        # Crear una nueva instancia del cliente MQTT
        client = mqtt.Client()

        # Conectar al broker
        client.connect(broker, port)

        # Publicar un mensaje para encender el LED
        client.publish(topic, led_indicator)
        if (led_indicator == 2): 
            client.publish("academics/IoT2", "Funciona Correctamente")

        # Desconectar del brokers
        client.disconnect()

        # Si es 0 se enciende ROJO, si es 1 se enciende VERDE
        if random_number1 == 0:
            led1_state.current.content = ft.Image(
                src='../assets/LED_OFF.png',
                scale=ft.Scale('1')
            )
        else:
            led1_state.current.content = ft.Image(
                src='../assets/LED_ON.jpg',
                scale=ft.Scale('1')
            )
        
        if random_number2 == 0:
            led2_state.current.content = ft.Image(
                src='../assets/LED_OFF.png',
                scale=ft.Scale('1')
            )
        else:
            led2_state.current.content = ft.Image(
                src='../assets/LED_ON.jpg',
                scale=ft.Scale('1')
            )

        if led_indicator != 2:
            show_error_message()
        
        led1_state.current.update()
        led2_state.current.update()
    
    def reset_leds(e):
        led1_state.current.content = ft.Image(
            src='../assets/LED.jpg',
            scale=ft.Scale('1')
        )
        led2_state.current.content = ft.Image(
            src='../assets/LED.jpg',
            scale=ft.Scale('1')
        )
        led1_state.current.update()
        led2_state.current.update()
        hide_error_message(e)
        
    # Botones para el funcionamiento del simulador del sistema experto
    Simular = ft.Container(
        content=ft.TextButton(text="Simular", on_click=toggle_leds),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=16,
        alignment=ft.alignment.center,
    )
    
    Reiniciar = ft.Container(
        content=ft.TextButton(text="Reiniciar", on_click=reset_leds),
        border=ft.border.all(1, ft.colors.BLACK),
        padding=16,
        alignment=ft.alignment.center,
    )
    
    # Crear contenedor para el mensaje de error
    error_container = ft.Container(
        ref=error_message_container,
        content=ft.Text(""),
        bgcolor=ft.colors.RED_200,
        padding=8,
        visible=False,
        alignment=ft.alignment.center,
    )
    
    # Añadir componentes al layout
    page.add(
        ft.Column([
            ft.Column([error_container]),
            ft.Row([
                ft.Container(width=500),
                title,
            ]),
            ft.Row([
                ft.Container(width=410),
                subtitle,
            ]),
            ft.Row([
                ft.Container(width=200),
                sram_controller,
                compare,
                internal_sram,
            ]),
            ft.Row([
                ft.Container(width=410),
                ft.Icon(name=ft.icons.ARROW_UPWARD , color=ft.colors.WHITE, size=30),
                ft.Container(width=75),
                ft.Icon(name=ft.icons.ARROW_UPWARD , color=ft.colors.WHITE, size=30),
                ft.Container(width=10),
                ft.Icon(name=ft.icons.ARROW_DOWNWARD , color=ft.colors.WHITE, size=30),
                ft.Container(width=90),
                ft.Icon(name=ft.icons.ARROW_DOWNWARD , color=ft.colors.WHITE, size=30),
            ]),
            ft.Row([
                ft.Container(width=720),
                clipper,
            ]),
            ft.Row([
                ft.Container(width=740),
                ft.Icon(name=ft.icons.ARROW_DOWNWARD , color=ft.colors.WHITE, size=30),
            ]),
            ft.Row([
                Input_Data,
                formatter_in,
                ft.Container(ref=led1_state, bgcolor=ft.colors.BLACK, height=60, width=60),
                ft.Icon(name=ft.icons.ADD , color=ft.colors.WHITE, size=30),
                decoder,
                ft.Icon(name=ft.icons.ADD , color=ft.colors.WHITE, size=30),
                ft.Container(width=135),
                scaler_rotator,
                ft.Icon(name=ft.icons.ARROW_FORWARD , color=ft.colors.WHITE, size=30),
                palette,
            ]),
            ft.Row([
                ft.Container(width=740),
                ft.Icon(name=ft.icons.ARROW_DOWNWARD , color=ft.colors.WHITE, size=30),
                ft.Container(width=100),
                ft.Icon(name=ft.icons.ARROW_DOWNWARD , color=ft.colors.WHITE, size=30),
            ]),
            ft.Row([
                ft.Container(width=875),
                padding,
            ]), 
            ft.Row([
                CLOCK_IN,
                pll,
                System_Clock,
                ft.Container(width=405),
                ft.Icon(name=ft.icons.SUBDIRECTORY_ARROW_RIGHT, color=ft.colors.WHITE, size=30),
                encoder,
                arrow_container,
                empty_container,
                ft.Container(ref=led2_state, bgcolor=ft.colors.BLACK, height=60, width=60),
                arrow_container2,
                empty_container2,
                ft.Icon(name=ft.icons.ARROW_FORWARD, color=ft.colors.WHITE, size=30),
                formatter_out,
                Output_Data
            ]),
            ft.Row([
                ft.Container(width=560),
                ft.Icon(name=ft.icons.SUBDIRECTORY_ARROW_RIGHT, color=ft.colors.WHITE, size=30),
                ft.Container(width=110),
                ft.Icon(name=ft.icons.ARROW_OUTWARD, color=ft.colors.WHITE, size=30),
                ft.Container(width=200),
            ]), 
            ft.Row([
                Control_Data,
                command_port_interface,
                ft.Container(width=90),
                ft.Icon(name=ft.icons.SUBDIRECTORY_ARROW_RIGHT, color=ft.colors.WHITE, size=30),
                ft.Container(width=265),
                ft.Icon(name=ft.icons.ARROW_OUTWARD, color=ft.colors.WHITE, size=30),
                ft.Container(width=450),
                Simular,
                Reiniciar
            ]),
        ])
    )

ft.app(target=main)
