import hashlib
secret="fdjlfkjdlgfhg;jfkje;lkjlkblkfjlgf" #一段沒有邏輯的亂碼，放 env
def generate_hash(text):
    sha = hashlib.sha256()
    sha.update((text+secret).encode("utf-8")) #雜湊後就看不到
    return sha.hexdigest()

def encodeToken(data):
    return data + "." + generate_hash(data)
def decodeToken(token):
    parts=token.split(".")
    if len(parts)==2:
        data=parts[0]
        hashshit=parts[1]
        print("hashshit: ", hashshit)
        checkHashshit = generate_hash(data)
        print("checkHashshit: ", checkHashshit)
        if checkHashshit == hashshit:
            return True
        else:
            return False
    else: 
        print("did not decode")
        return False


from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_303_SEE_OTHER
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="week7/practice_cookie/templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html",{
        "request": request,
        "title": "歡迎光臨，請輸入帳號密碼",
        "subtitle": "登入系統"
    })

@app.post("/signin")
async def signin(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "test" and password == "test":
        print(username, password, "success signin")
        response = RedirectResponse(url="/member", status_code=HTTP_303_SEE_OTHER)
        response.set_cookie("token", encodeToken("test"), max_age=600)
        return response
    else:
        print("error signin")
        response = RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
        response.set_cookie("token","", max_age=-1)
        return response


@app.get("/member")
def member(request: Request):
    token = request.cookies.get("token")
    if token == None:
        print("no token")
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    elif not decodeToken(token):
        print("error token")
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    else: 
        return templates.TemplateResponse("member.html", {
            "request": request,
            "title": "歡迎光臨，這是會員頁",
            "subtitle": "恭喜你，成功登入系統"
            })

@app.get("/signout")
def signout(request:Request):
    response = RedirectResponse("/", status_code=HTTP_303_SEE_OTHER)
    response.set_cookie("token", "", max_age=-1)
    return response

app.mount("/static", StaticFiles(directory="week7/practice_cookie/static"), name="static")
