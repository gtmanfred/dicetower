import fastapi.staticfiles
import fastapi.middleware.cors
import socketio

from . import __version__
from .config import Configuration as config
from .socketio import sio
from .utils.loader import load_handlers


def create_app(debug=False):
    app = fastapi.FastAPI(
        title=config.PROJECT_NAME,
        description=config.PROJECT_NAME,
        version=__version__,
        debug=debug,
    )

    sio_asgi_app = socketio.ASGIApp(
        socketio_server=sio,
        other_asgi_app=app
    )

    app.add_route("/socket.io/", route=sio_asgi_app, methods=['GET', 'POST'])
    app.add_websocket_route("/socket.io/", sio_asgi_app)
    app.mount(
        '/ui',
        fastapi.staticfiles.StaticFiles(directory='dicetower/static/', html=True, check_dir=False),
        name='webapp',
    )

    app.add_middleware(
        fastapi.middleware.cors.CORSMiddleware,
        allow_origins=config.ALLOW_ORIGINS_RND,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    load_handlers(app)

    return app
