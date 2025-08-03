from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['http://localhost:5173', 'http://192.168.52.1:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#                                   python -m uvicorn Main:app --reload

@app.get("/")
async def root(request: Request):
    return {'message':'ghgh'}