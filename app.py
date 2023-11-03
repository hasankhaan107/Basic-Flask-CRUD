import os

# App Initialization
from . import create_app # from __init__ file
app = create_app(os.getenv("CONFIG_MODE"))

# projects routes
from .projects import urls

if __name__ == "__main__":
    app.run()