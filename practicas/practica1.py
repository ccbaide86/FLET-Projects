import flet as ft
import time
from threading import Thread
import numpy as np

# Clase para los discos
class Disk(ft.Container):
    def __init__(self, width, index, color):
        super().__init__(
            width=width,
            height=20,
            bgcolor=color,
            border_radius=5,
            alignment=ft.alignment.center
        )
        self.index = index

# Clase para las varillas
class Rod(ft.Container):
    def __init__(self, rod_num):
        super().__init__(
            width=120,
            height=10,
            bgcolor=ft.colors.BLACK,
            border_radius=5,
            alignment=ft.alignment.bottom_center
        )
        self.rod_num = rod_num
        self.disks = []

# Función para mover discos
def move_disk(page, from_rod, to_rod, disk):
    from_rod.disks.remove(disk)
    to_rod.disks.append(disk)
    update_ui(page)
    page.update()
    time.sleep(1)  # Añadimos una pausa para ver el movimiento

# Algoritmo recursivo de Torres de Hanoi
def hanoi(page, n, from_rod, to_rod, aux_rod):
    if n == 1:
        disk = from_rod.disks[-1]
        move_disk(page, from_rod, to_rod, disk)
    else:
        hanoi(page, n - 1, from_rod, aux_rod, to_rod)
        hanoi(page, 1, from_rod, to_rod, aux_rod)
        hanoi(page, n - 1, aux_rod, to_rod, from_rod)

# Función para actualizar la interfaz gráfica
def update_ui(page):
    page.controls.clear()
    
    rod_containers = [ft.Column([ft.Container(width=200, height=20) for _ in range(7)]) for _ in range(3)]

    for rod in rods:
        for idx, disk in enumerate(rod.disks):
            rod_containers[rod.rod_num].controls[6 - idx] = disk
    
    row = ft.Row(controls=[
        ft.Column([rod_containers[0], rods[0]], alignment=ft.alignment.center),
        ft.Column([rod_containers[1], rods[1]], alignment=ft.alignment.center),
        ft.Column([rod_containers[2], rods[2]], alignment=ft.alignment.center)
    ], alignment=ft.alignment.center)
    
    container = ft.Container(
        content=row,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center
    )

    # Contenedor del botón de reinicio
    reset_button = ft.ElevatedButton(
        text="Reiniciar Juego",
        on_click=lambda e: reset_game(page)
    )

    # Contenedor del botón de posición aleatoria
    randomize_button = ft.ElevatedButton(
        text="Posición Aleatoria",
        on_click=lambda e: randomize_disks(page)
    )

    button_container = ft.Container(
        content=ft.Row([reset_button, randomize_button], alignment=ft.alignment.center),
        alignment=ft.alignment.center,
        margin=10
    )
    
    page.add(container)
    page.add(button_container)
    page.update()

# Función para reiniciar el juego
def reset_game(page):
    global rods
    num_disks = 4
    rods = [Rod(i) for i in range(3)]
    
    # Colores para los discos
    disk_colors = [ft.colors.ORANGE, ft.colors.BLUE, ft.colors.YELLOW, ft.colors.RED]
    
    # Inicializamos los discos en la primera varilla
    for i in range(num_disks, 0, -1):
        color = disk_colors[i % len(disk_colors)]
        disk = Disk(width=40 + i * 20, index=i, color=color)
        rods[0].disks.append(disk)
    
    # Inicializamos la UI
    update_ui(page)
    
    # Ejecutamos el algoritmo de Hanoi en un hilo separado para no bloquear la UI
    def run_hanoi():
        hanoi(page, num_disks, rods[0], rods[2], rods[1])

    thread = Thread(target=run_hanoi)
    thread.start()

# Función para colocar los discos en posiciones aleatorias
def randomize_disks(page):
    global rods
    num_disks = 4
    rods = [Rod(i) for i in range(3)]
    
    # Colores para los discos
    disk_colors = [ft.colors.ORANGE, ft.colors.BLUE, ft.colors.YELLOW, ft.colors.RED]
    
    # Generamos posiciones aleatorias para los discos
    random_positions = np.random.choice(3, num_disks, replace=True)
    
    for i in range(num_disks, 0, -1):
        color = disk_colors[i % len(disk_colors)]
        disk = Disk(width=40 + i * 20, index=i, color=color)
        rods[random_positions[i - 1]].disks.append(disk)
    
    # Actualizamos la UI
    update_ui(page)

# Main app
def main(page: ft.Page):
    global rods
    page.title = "Torres de Hanoi"
    page.vertical_alignment = ft.alignment.center
    page.horizontal_alignment = ft.alignment.center

    num_disks = 4
    rods = [Rod(i) for i in range(3)]
    
    # Colores para los discos
    disk_colors = [ft.colors.ORANGE, ft.colors.BLUE, ft.colors.YELLOW, ft.colors.RED]
    
    # Inicializamos los discos en la primera varilla
    for i in range(num_disks, 0, -1):
        color = disk_colors[i % len(disk_colors)]
        disk = Disk(width=40 + i * 20, index=i, color=color)
        rods[0].disks.append(disk)
    
    # Inicializamos la UI
    update_ui(page)
    
    # Ejecutamos el algoritmo de Hanoi en un hilo separado para no bloquear la UI
    def run_hanoi():
        hanoi(page, num_disks, rods[0], rods[2], rods[1])

    thread = Thread(target=run_hanoi)
    thread.start()

ft.app(target=main)

