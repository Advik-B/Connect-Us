from pynecone import *

sidebar = lambda: box(
    vstack(
        text(
            "Connect Us",
            font_size="1.5rem",
            font_family="JetBrains Mono",
            font_weight="bold",
        ),

        button(
            "Home",
            font_size="1rem",
            font_family="JetBrains Mono",
            font_weight="bold",
            color="white",
            border="1px solid white",
            border_radius="5px",
            padding="5px",
            margin="5px",
            background_color="black",
        ),
    ),
    background_color="black",
    color="white",
    padding="10px",
    margin="10px",
    border="1px solid white",
    border_radius="5px",
    position="absolute",
    top="0px",
    left="0px",
    width="200px",
    height="100%",

)