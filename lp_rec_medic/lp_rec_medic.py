import reflex as rx
from lp_rec_medic.contenido.navbar import navbar
from lp_rec_medic.contenido.header import header
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        navbar(),
        header(),
        width="100vw",
        height="100vh",
    )
    
    

app = rx.App()
app.add_page(index)

