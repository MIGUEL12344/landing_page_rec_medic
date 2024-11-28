import reflex as rx

def header()-> rx.Component:
    return rx.vstack(
        rx.heading("Bienvenido a Salud Notifica",
                size="9",
                font_weigth="10",
                style={
                    "background": "linear-gradient(to right, #C0C0C0, #B0B0B0)",
                    "-webkit-background-clip":"text",
                    "color":"transparent"
                }),
        
        rx.hstack(
            rx.image(src="/mewing.png", width="300px", height="300px",margin_top="-203px",margin_left="-170px"),
            rx.text("""¡Nunca más olvides tomar tus medicamentos! Con nuestra innovadora aplicación de recordatorio,
                     tu salud está en buenas manos. Configura recordatorios personalizados,
                     recibe notificaciones oportunas y lleva un seguimiento detallado de tu medicación diaria.
                     Ideal para todas las edades, nuestra app es fácil de usar y garantiza que nunca te saltes una dosis.
                     ¡Descarga ahora y toma el control de tu bienestar!""",
                justify_items="center",
                size="7",
                margin_top="100px",
                font_family="bold",
                color="#c56dfc",
                style={
                    "whiteSpace":"pre-line"}),
                rx.spacer(),
            rx.image(src="/minions.png", width="400px", height="400px",margin_top="-50px",margin_right="-50px"),
            width="86vw"
        ),
        rx.link(
            rx.button("DESCARGAR",
                      background="gray",
                      _hover={
                          "background":"rgba(197, 109, 252, 0.5)"}),
            href="https://www.youtube.com/",
            margin_top="80px",
        ),
        align="center",
        justify="center",
        margin_top="130px",
    )