from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import Base, Banner, User, GameDeepInfo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette import status
from Other_functions import CheckText, GenPassword
import Neironet
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

current_user = ''

class Item(BaseModel):
    name: str

class UserId(BaseModel):
    id: int

@app.post('/Custom')
async def root(req: Item):
    print(req.name)

@app.get('/')
async def root(req: Request, res: Response):
    banner_id = req.query_params.get('banner') or 1
    banner_exists = db_session.query(Banner).filter_by(id=banner_id).first()
    
    if banner_exists: 
        return {'message': banner_exists}
    else: 
        res.status_code= status.HTTP_404_NOT_FOUND
        return {'message': 'banner not found'}

@app.get('/GetGameCards')
async def root(req: Request, res: Response):
    info_id = req.query_params.get('info_id') or 1
    

@app.get('/Catalog')
async def root(req: Request, res: Response):
    banner_id = req.query_params.get('banner') or 1
    banner_exists = db_session.query(Banner).filter_by(id=banner_id).first()
    
    if banner_exists: 
        return {'message': banner_exists}
    else: 
        res.status_code= status.HTTP_404_NOT_FOUND
        return {'message': 'banner not found'}


@app.post('/Enter')
async def root(req: Request, res: Response):
    username = req.query_params.get('username')
    password = req.query_params.get('password')
    user_password = db_session.query(User).filter_by(username=username).first()
    
    if user_password and username and password:
        if user_password == password:
            return {'message': 'Регистрация прошла успешно!'}
        else:
            return {'message': 'Неправильный юзернейм или пароль!'}
    else:
        res.status_code= status.HTTP_404_NOT_FOUND
        return {'message': 'banner not found'}

@app.post('/Registration')
async def root(req: Request, res: Response):
    username = req.query_params.get('username')
    password = req.query_params.get('password')
    e_mail = req.query_params.get('email')
    type_of_account = req.query_params.get('type_of')
    
    Check = False
    
    if username and password and e_mail and type_of_account and Check:
        pass

@app.get('/RecommendedGame')
async def root(req: Request, res: Response):
    game_tags = req.query_params.get('tags') or 'шутер, зомби'
    game,conf = Neironet.recommend_game(game_tags)
    
    if game and conf:
        return {'message': game}
    else:
        res.status_code= status.HTTP_404_NOT_FOUND
        return {'message': 'banner not found'}
         

@app.get('/GamePage')
async def root(req: Request, res: Response):
    user_id = req.query_params.get('id') or 1
    banner_exists = db_session.query(Banner).filter_by(id=user_id).first()
    
    print(banner_exists)
    
    if banner_exists: 
        return {'message': banner_exists}
    else: 
        res.status_code= status.HTTP_404_NOT_FOUND
        return {'message': 'banner not found'}

@app.get('/GameDeepInfo')
async def root(req:Request, res:Response):
    game_id = req.query_params.get('id') or 1
    banner_exists = db_session.query(GameDeepInfo).filter_by(game_id=game_id).first()
    if banner_exists: 
        return {'message': banner_exists}
    else: 
        res.status_code= status.HTTP_404_NOT_FOUND
        return {'message': 'banner not found'}

@app.post('/Registration')
async def root(req:Request, res: Response):
    return {'message': 'message'}
    user = req.query_params.get('username')
    pw = req.query_params.get('password')
    type_of_acc = req.query_params.get('type')
    email = req.query_params.get('email') 
    
    message = 'Not found'
    
    
    if user and pw and type_of_acc and email:
        banner_exists = db_session.query(User).filter_by(username=user).first()
        
        if banner_exists:
            return {'message': 'user exists!'}
        else:
            new_user = User(username=user, password=pw, account_type = type_of_acc)
            
            try:
                db_session.rollback()
                
                current_user = user
                
                db_session.add(new_user)
                db_session.commit()
                message = 'Вы успешно зарегестрировались'
            except: 
                message = 'Ошибка'
            finally:
                db_session.close()
                 
    return {'message': message}
    


@app.post('/')
async def root(req:Request):
    return {'message': 'Прошёл запрос'}

@app.get('/GenPassword')
async def root(req: Request, res: Response):
    new_pass = GenPassword(30)
    if new_pass:
        return {'message': new_pass}
