# coding:utf-8
import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from service.blue_code_service import BlueCodeService

app = FastAPI()
blue_code_service = BlueCodeService()

# 挂载静态资源
app.mount("/static", StaticFiles(directory="static"), name="static")

# 创建模板
template = Jinja2Templates("template")


@app.get("/")
def blue_code(request: Request):
    text = blue_code_service.get_text()
    return template.TemplateResponse("index.html", {"request": request, "text": text})


if __name__ == '__main__':
    uvicorn.run(app, port=9090)
