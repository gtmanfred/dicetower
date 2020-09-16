import fastapi.staticfiles
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
        '/html',
        fastapi.staticfiles.StaticFiles(directory='dicetower/static/html', html=True),
        name='html',
    )
    app.mount(
        '/js',
        fastapi.staticfiles.StaticFiles(directory='dicetower/static/js', html=True),
        name='javascript',
    )
    app.mount(
        '/css',
        fastapi.staticfiles.StaticFiles(directory='dicetower/static/css', html=True),
        name='styles',
    )

    load_handlers(app)

    return app
