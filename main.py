import flet as ft

def main(page: ft.Page): 
    page.title = "Calculadora de Propina" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

txt_monto = ft.TextField(
    label="Monto de cuenta ($)",
    width=200,
    text_align=ft.TextAlign.RIGHT
)

txt_propina = ft.Text("Propina: $0.00", size=16)
txt_total = ft.Text("Total a pagar: $0.00", size=18, weight=ft.FontWeight.BOLD)

def calcular(porcentaje):
    try:
        monto = float(txt_monto.value)
        propina = monto * porcentaje
        total = monto + propina

        txt_propina.value = f"Propina: ${propina:.2f}"
        txt_total.value = f"Total a pagar: ${total:.2f}"
        page.update()
    except:
        txt_propina.value = "Propina: $0.00"
        txt_total.value = "Total a pagar: $0.00"
        page.update()

btn_5 = ft.ElevatedButton(
    "5%",
    on_click=lambda e: calcular(0.05)
)

btn_25 = ft.ElevatedButton(
    "25%",
    on_click=lambda e: calcular(0.25)
)

page.add(
    ft.Column(
        [
            ft.Text("Monto de cuenta", size=20, weight=ft.FontWeight.BOLD),
            txt_monto,
            ft.Row(
                [btn_5, btn_25],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            txt_propina,
            txt_total,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
)
ft.app(target=main)
