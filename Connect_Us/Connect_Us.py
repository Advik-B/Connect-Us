"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from .index import index
from .sidebar import sidebar


class State(pc.State):
    """The app state."""

    pass


app = pc.App(state=State, )
app.add_page(index, title="Home")
app.compile()
