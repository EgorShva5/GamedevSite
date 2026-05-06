import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from database import Base, Banner, User, GameDeepInfo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

games = []
all_tags = [
    "шутер", "открытый мир", "ролевая игра", 
    "выживание",
    "строительство", "зомби", "сюжет",
    "гонки", "ферма", "фентези", 'aркада',
    'мультиплеер',
    'нелинейная', 'рогалик'  
]

data = {}

engine = create_engine('sqlite:///./Test.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()


def _create_data():
    data = {}
    games = []
    db_data = db_session.query(GameDeepInfo).all()
    for i in db_data:
        data[i.game_id] = i.tags.split(',')
        games.append(i.game_id)
        
    return (data, games)

data, games = _create_data()

print(data,games)


X = np.array([data[game] for game in games], dtype=np.float32)
y = np.array([games.index(game) for game in games])
y_onehot = to_categorical(y, num_classes=len(games))

MODEL_FILENAME = "neironet/game_recommender_model.keras" 

def create_model():
    model = Sequential([
        Dense(8, activation='relu', input_shape=(len(all_tags),)),
        Dense(len(games), activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

if os.path.exists(MODEL_FILENAME):
    model = load_model(MODEL_FILENAME)
else:
    model = create_model()
    model.fit(X, y_onehot, epochs=200, verbose=1)
    model.save(MODEL_FILENAME)

def recommend_game(tags_str):
    input_tags = [tag.strip().lower() for tag in tags_str.split(',')]
    vector = np.zeros(len(all_tags), dtype=np.float32)
    for i, tag in enumerate(all_tags):
        if tag in input_tags:
            vector[i] = 1.0
    probs = model.predict(vector.reshape(1, -1), verbose=0)[0]
    best_idx = np.argmax(probs)
    confidence = probs[best_idx]
    return games[best_idx], confidence