from aiohttp import web
import hvac

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
"""

client = hvac.Client(url="http://localhost:8300") # TODO: move from global


def handle_endpoint(endpoint): # REFACTOR: async?
    if "login" in endpoint.split(r"/"):
        return endpoint.split(r"/")[-1]
    else:
        return None


def is_valid_user(login, password): # REFACTOR: async?
    login_response = client.auth.userpass.login(
        username=login,
        password=password,
    )
    return client.is_authenticated()


# TODO: rotation_postfix in login and password

# TODO: check password lease -> notify user or send token
async def handle(request):
    login = handle_endpoint(request.match_info.get("key"))  # if None
    request_body = (
        await request.json()
    )  # if None / TypeError: 'coroutine' object is not subscriptable
    password = request_body["password"]
    validation_result = is_valid_user(login, password)

    # check if kv expired
    res = client.auth.userpass.update_password_on_user(login, password) # TODO: try except => rights

    # TODO: Typing
    response = {
        # "request_id":"ec73e1b5-45cc-eef1-f2a1-353d26b958ed",
        # "lease_id":"",
        # "renewable":False,
        # "lease_duration":0,
        # "data":None,
        # "wrap_info":None,
        # "warnings":None,
        "auth": {
            "client_token": client.token, # "UPDATE_PASSWORD! USE POSTFIX 'rotate' for update. For example: userX_rotate:oldpassword_newpassword"
            # "accessor":"SLHcCT66EKBJddoyCdLNqBmX",
            # "policies":["admins","default"],
            # "token_policies":["admins","default"],
            # "metadata":{"username":"test"},
            # "lease_duration":2764800,
            # "renewable":True,
            # "entity_id":"aa5bfcd3-80ef-96e8-a4ee-5726549511b7",
            # "token_type":"service",
            # "orphan":True
        }
    }

    return web.json_response(response)


app = web.Application()

# TODO: move endpoints 
app.add_routes(
    [web.get("/", handle), web.put("/{key:.+}", handle), web.get("/{name}", handle)]
)
app.add_routes([web.route("*", "/path", handle)])

if __name__ == "__main__":
    web.run_app(app)
