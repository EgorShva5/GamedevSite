from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


# uvicorn Main:app --reload --host 0.0.0.0 --port 8000
app = FastAPI()

IPs   : list[str] = ['localhost', '192.168.52.1', '192.168.100.22']
Port  : int       = 5173
Secure: bool      = False

origins = [f"{'https' if Secure else 'http'}://{i}:{Port}" for i in IPs]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str

@app.post('/Custom')
async def root(req: Item):
    print(req.name)

@app.get('/')
async def root(req: Request):
    return {'message':'hello from backend!'}

@app.get('/Custom')
async def root2(req: Request):
    return {'message':'hi'}
