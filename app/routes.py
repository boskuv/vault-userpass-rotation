from aiohttp import web
from app import views

def setup_routes(app):
    #app.router.add_get("/", views.index)
    app.add_routes(
        [web.get("/", views.handle), web.put("/{key:.+}", views.handle), web.get("/{name}", views.handle)]
    )
    app.add_routes([web.route("*", "/path", views.handle)]) # to config