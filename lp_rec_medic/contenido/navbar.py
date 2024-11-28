import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("S-Notifica",
                font_weight="bold",
                margin_top="10px",
                font_size="30px",
                color="#c56dfc",
                margin_left="20px"),
        rx.spacer(),
        rx.color_mode.button(position="center",
                             margin_top="15px"),
        rx.spacer(),
        rx.link(
            rx.button(
            "Redes Sociales",
            background="transparent",
            margin_top="15px",
            color="#c56dfc",
            size="3",
            _hover={
                "color":"rgba(255, 0, 0, 0.5)"},
            style={
            "border_left":"2px solid #c56dfc"},
            ),
            href="youtube.com"),
        rx.link(
            rx.button(
            "Acerca de",
            background="transparent",
            margin_top="15px",
            color="#c56dfc",
            size="3",
            _hover={
                "color":"rgba(255, 0, 0, 0.5)"},
            style={
            "border_left":"2px solid #c56dfc"},
            ),
            href="youtube.com"),
        rx.link(
            rx.button(
            "Contactanos",
            background="transparent",
            margin_top="15px",
            margin_right="20px",
            color="#c56dfc",
            size="3",
            _hover={
                "color":"rgba(255, 0, 0, 0.5)"},
            style={
            "border_left":"2px solid #c56dfc"},
            ),
            href="youtube.com"),
        position="sticky",
        bg="white",
        justify="end",
        background = "transparent",
        style={
            "border_bottom":"4px solid #c56dfc"
        }
    )