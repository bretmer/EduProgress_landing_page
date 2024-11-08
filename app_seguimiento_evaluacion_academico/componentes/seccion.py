import reflex as rx
def seccion()->rx.components:
    return rx.vstack(
        rx.heading(
            rx.text("EduProgress",size="9"),
            rx.text("La aplicacion que necesitas",size="4")
        ),
        rx.container(
            rx.text("Con esta aplicacion tendras un manejo de tu progreso  ", color=rx.color("blue",10)),
            rx.text("academico en tiempo real, monitoriado por un profesional",color=rx.color("blue",10)),
            rx.link(rx.button("REGISTRARME", margin_top="4em"),href="/#",variant="outline"),
            margin_top="1em"
        ),
        padding_top="8em",
        align="center",
        text_align="center",
        beight="800px"
        

    )