import reflex as rx
def seccion()->rx.components:
    return rx.vstack(
        rx.vstack(
            rx.heading("EduProgress",size="9"),
            rx.text("La aplicacion que necesitas",size="5",weight="bold"),
            align="center",
            margin_top="2em"
        ),
        rx.container(
            rx.hstack(
                rx.text("Con esta aplicacion tendras un manejo de tu progreso academico en tiempo real, monitoriado por un docente, tambien podras visualizar tu avance y podras gestionar informes sobre el progreso de tu avance",color=rx.color("blue",10),
                margin_top="2em",
                weight="bold",
                size="5"
                ),
                rx.image(src="https://www.itsitio.com/wp-content/uploads/2019/04/04052020-itsitio-portada-780x405.jpg",
                width="350px",
                margin_top="1em",
                align_items="center" 
                ),
                spacing="4em"
            ),         
                rx.link(
            rx.button("REGISTRARME",size="4", margin_top="4em"),
            href="https://forms.gle/LUkeqyazppTBapbZA",variant="outline",
            is_external=True),            
        ),
        padding_top="2em",
        align="center",
        text_align="center",
        height="676px",
        background=rx.color("slate",5),

    )