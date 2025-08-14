from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import Base, Banner
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette import status

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

engine = create_engine('sqlite:///./Test.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()

#NewBanner = Banner(title='Тест1', description='Описание1', linkpath='https://google.com', imgpath='путь')

#db_session.add(NewBanner)
#db_session.commit()
#db_session.close()

class Item(BaseModel):
    name: str

@app.post('/Custom')
async def root(req: Item):
    print(req.name)

@app.get('/')
async def root(req: Request, res: Response):
    banner_id = req.query_params.get('banner') or 1
    banner_exists = db_session.query(Banner).filter_by(id=banner_id).first()
    
    print(banner_exists)
    
    if banner_exists: 
        return {'message': banner_exists}
    else: 
        res.status_code= status.HTTP_404_NOT_FOUND
        return {'message': 'banner not found'}

@app.post('/')
async def root(req:Request):
    pass

@app.get('/Custom')
async def root2(req: Request):
    return {'message':'hi'}
