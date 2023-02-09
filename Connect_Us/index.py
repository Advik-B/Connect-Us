from pynecone import text, center


def index():
    return center(
        text(
            "Hello world!",
            font_size="2rem",
            font_weight="bold",
        )
    )
