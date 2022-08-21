
'''
Created on 

Course work: 

@author: 

Source:

'''

# Import necessary modules
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/",)  # Base api
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



if __name__ == '__main__':
    # print("Please Run FastAPI as mentioned in README file")

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8800,
        reload=True,
        access_log=False
    )
