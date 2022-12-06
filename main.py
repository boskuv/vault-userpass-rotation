"""
TODO:
vault instanse on different port
policy for updating

https://hvac.readthedocs.io/en/stable/_modules/hvac/api/auth_methods/userpass.html
https
password = getpass.getpass() / print(password)
Typing
requests.exceptions.ReadTimeout: HTTPConnectionPool
aiojobs or kv with dates
__all__
"""
from aiohttp import web

from app.routes import setup_routes

def setup_app(application):
    setup_routes(application)
    print('app is OK')


app = web.Application()

if __name__ == "__main__":
    setup_app(app)
    web.run_app(app)
