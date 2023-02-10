from pynecone import *
from .sidebar import sidebar

def index():
    return box(
        sidebar(),
        vstack(
            text(
                "Welcome to Connect Us!",
                font_size="1.5rem",
                font_family="JetBrains Mono",
                font_weight="bold",
            ),
            text(
                "This is a simple app that allows you to connect with other people.",
                font_size="1rem",
                font_family="JetBrains Mono",
                font_weight="bold",
            ),
        )
    )



