import flet as ft
from app.styles.estilos import Buttons, Card, Colors, Inputs, Textos
from app.components.popup import show_popup

def home_view(page: ft.Page):
    titulo = ft.Text("Mi app con estilos", style=Textos.H1)
    subtitulo = ft.Text("Aplicacion pedir producto", style=Textos.H2)

    nombre = ft.TextField(label="Producto", **Inputs.INPUT_PRIMARY)
    precio = ft.TextField(label="Precio", keyboard_type=ft.KeyboardType.NUMBER, **Inputs.INPUT_PRIMARY)
    cantidad = ft.TextField(label="Cantidad", keyboard_type=ft.KeyboardType.NUMBER, **Inputs.INPUT_PRIMARY)

    resultado = ft.Text("", style=Textos.H3)

    async def on_click(e):
        try:
            p = float(precio.value)
            c = float(cantidad.value)
            total = p * c

            resultado.value = f"""
Producto: {nombre.value}
Precio: {p}
Cantidad: {c}
Total: {total}
"""
            page.update()

        except:
            await show_popup(page, "Error", "Ingresa valores numéricos válidos", bgcolor=Colors.DANGER)

    btn = ft.Button("Calcular", style=Buttons.BUTTON_PRIMARY, on_click=on_click)

    columna = ft.Column(
        controls=[titulo, subtitulo, nombre, precio, cantidad, btn, resultado],
        spacing=16
    )

    card = ft.Container(content=columna, **Card.tarjeta)

    return ft.Container(
        padding=10,
        alignment=ft.Alignment(0, 0),
        content=card
    )