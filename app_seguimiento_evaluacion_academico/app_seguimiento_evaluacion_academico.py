import reflex as rx
from .componentes.navbar import navbar
from .componentes.seccion import seccion
def index ()->rx.components:
    return rx.box(
        navbar(),
        seccion()
    )

app=rx.App()
app.add_page(index)