'''
Created on : 21 Aug 2022

@author: Sivaraam T K, Vikram M, Elakia VM

Source:

'''

# Import necessary modules
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn

from scraper import raw

app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/form",)  # Base api
def home_api():

    result_dict = {
        "hello": "world"
    }

    return result_dict

@app.get("/test")
def read_item(num: int):
    result = num * 2
    return {
        "num"   : num,
        "number_twice": result
        }

@app.get("/")
def form_post(request: Request):
    result = {
        'message': "Enter the URL"
    }
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


# @app.post("/form")
# def form_post(request: Request, link: str = Form(...)):
#     result = result = {
#         'message': f"The URL Entered is {link}"
#     }
#     return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post("/view")
def view_post(request: Request, link: str = Form(...)):
    
    content = raw(link)

    result = {
        'content': content,
        'message': f"The URL Entered is {link}"
    }
    return templates.TemplateResponse('view.html', context={'request': request, 'result': result})


if __name__ == '__main__':
    # Please Run FastAPI as mentioned in README file

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        access_log=False
    )