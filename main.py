import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora de Propina"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    txt_monto = ft.TextField(
        label="Monto de cuenta ($)",
        width=200,
        text_align=ft.TextAlign.RIGHT,
    )

    txt_propina = ft.Text("Propina: $0.00", size=16)
    txt_total = ft.Text(
        "Total a pagar: $0.00",
        size=18,
        weight=ft.FontWeight.BOLD,
    )

    # 🔹 Slider entre 10% y 30% con 8 opciones
    slider = ft.Slider(
        min=10,
        max=30,
        divisions=7,  # 8 valores
        value=10,
        label="{value}%",
    )

    def calcular(e):
        try:
            monto = float(txt_monto.value)
            porcentaje = slider.value / 100
            propina = monto * porcentaje
            total = monto + propina

            txt_propina.value = f"Propina: ${propina:.2f}"
            txt_total.value = f"Total a pagar: ${total:.2f}"
        except:
            txt_propina.value = "Propina: $0.00"
            txt_total.value = "Total a pagar: $0.00"

        page.update()

    slider.on_change = calcular

    page.add(
        ft.Column(
            [
                ft.Text("Monto de cuenta", size=20, weight=ft.FontWeight.BOLD),
                txt_monto,
                slider,
                txt_propina,
                txt_total,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.run(main)
