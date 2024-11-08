import reflex as rx

def navbar()-> rx.components:
    return rx.hstack(
        rx.hstack(
            rx.heading("EduProgress", size="6",weight="bold", color="white")
        ),
        padding="1em",
        width="100%",
        bg="red"
    )