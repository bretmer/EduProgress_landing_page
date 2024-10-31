import reflex as rx
# crear el componente principal de mi pagina
def index ()->rx.components:
    return rx.text("hola mundo")

# instanciar la clase app de reflex
app=rx.App()
app.add_page(index)