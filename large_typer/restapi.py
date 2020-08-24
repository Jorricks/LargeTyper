from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse, UJSONResponse, RedirectResponse


__all__ = (
    "app"
)

from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from . import settings
from .controller import Controller

controller = Controller()


routes = [
    Mount('/static/', app=StaticFiles(directory='static/'), name="static"),
]

app = Starlette(debug=settings.DEBUG, routes=routes)


@app.route("/")
async def homepage(request: Request) -> RedirectResponse:
    if request.client.host in [settings.IP, 'localhost', '127.0.0.1']:
        return RedirectResponse(url='/static/host/index.html')
    return RedirectResponse(url='/static/client/index.html')


@app.route("/ping")
async def ping(_: Request) -> PlainTextResponse:
    """
    responses:
      "200":
        description: Check the presence of the service.
        content:
          text/plain:
            schema:
              type: string
              example: pong
    """
    return PlainTextResponse("pong")


@app.route("/forecast")
async def forecast(request: Request) -> UJSONResponse:
    """
    """

    return UJSONResponse({
        "forecast": None
    })
