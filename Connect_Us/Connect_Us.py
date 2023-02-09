"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from .index import index

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


app = pc.App(state=State)
app.add_page(index)
app.compile()
