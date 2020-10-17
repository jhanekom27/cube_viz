import os
from dotenv import load_dotenv

from cubeviz.server import app
from cubeviz.layout import build_app
import cubeviz.callback

load_dotenv()


if __name__ == "__main__":
    app = build_app(app)

    environment = os.getenv("ENVIRONMENT")
    if environment == "local":
        app.run_server(host="127.0.0.1", port=8000, debug=True)
    else:
        app.run_server()
