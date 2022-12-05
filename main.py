from aiohttp import web
"""
TODO:
https://hvac.readthedocs.io/en/stable/_modules/hvac/api/auth_methods/userpass.html
https
"""

# TODO: check password lease -> notify user or send token
async def handle(request):
    print(request) # request.match_info.get(
    #text = "Hello, " + name
    response = {
    # "request_id":"ec73e1b5-45cc-eef1-f2a1-353d26b958ed",
    # "lease_id":"",
    # "renewable":False,
    # "lease_duration":0,
    # "data":None,
    # "wrap_info":None,
    # "warnings":None,
    "auth":{
    #"client_token":"s.gjX6toE2E4xpp1Y2LRS2qFgL",
    #"accessor":"SLHcCT66EKBJddoyCdLNqBmX",
    #"policies":["admins","default"],
    #"token_policies":["admins","default"],
    #"metadata":{"username":"test"},
    #"lease_duration":2764800,
    #"renewable":True,
    #"entity_id":"aa5bfcd3-80ef-96e8-a4ee-5726549511b7",
    #"token_type":"service",
    #"orphan":True
    }
    }
    return web.json_response(response)


app = web.Application()
app.add_routes([web.get('/', handle),
                web.put('/{key:.+}', handle),
                web.get('/{name}', handle)])
app.add_routes([web.route('*', '/path', handle)])


if __name__ == '__main__':
    web.run_app(app)