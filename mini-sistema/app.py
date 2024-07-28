import flet as ft
import requests

def main(page: ft.Page):
    def send_data(e):
        data = {"message": "0"}
        response = requests.post("http://localhost:1880/flet", json=data)
        print(response.text)

    btn_send = ft.ElevatedButton(text="Send Data", on_click=send_data)
    page.add(btn_send)

ft.app(target=main)
