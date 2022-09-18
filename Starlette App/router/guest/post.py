from starlette.requests import Request
from starlette.responses import RedirectResponse

from helper import body_as_json
from database.models import User
from database.main import session
from authentication import login_user

from http import HTTPStatus

async def internal_register(request: Request):
    
    body = await body_as_json(request, ["username", "password"])
    
    username_ = body.get("username")
    password_ = body.get("password")

    session.add(User(username=username_, password=password_))
    
    session.commit()
    
    return RedirectResponse("/signin", HTTPStatus.FOUND)
    
async def internal_signin(request: Request):
    
    body = await body_as_json(request, ["username", "password"])
    
    username_ = body.get("username")
    password_ = body.get("password")
    
    user = session.query(User).filter_by(username = username_).first()
    
    if user is None or user.password != password_:
        
        return RedirectResponse("/", HTTPStatus.FOUND)
    
    else:

        return login_user(RedirectResponse("/", HTTPStatus.FOUND), user.id_)