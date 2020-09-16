import inspect

import asgi_lifespan
import httpx
import pytest

from dicetower.app import create_app


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(config, items):
    for item in items:
        if inspect.iscoroutinefunction(item.function):
            item.add_marker(pytest.mark.asyncio)


@pytest.fixture
async def app():
    app = create_app(debug=True)
    async with asgi_lifespan.LifespanManager(app):
        yield app


@pytest.fixture
async def client(app):
    async with httpx.AsyncClient(app=app, base_url='http://dicetower.app/') as client:
        yield client
