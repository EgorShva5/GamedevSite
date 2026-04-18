import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import os

# ----- 1. Подготовка данных -----
games = ["DOOM", "Minecraft", "The Witcher 3", "GTA V", "Stardew Valley"]

all_tags = [
    "шутер", "открытый мир", "ролевая игра", "выживание",
    "строительство", "зомби", "сюжет", "гонки", "ферма", "магия"
]

data = {
    "DOOM":           [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    "Minecraft":      [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    "The Witcher 3":  [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    "GTA V":          [1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    "Stardew Valley": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
}

X = np.array([data[game] for game in games], dtype=np.float32)
y = np.array([games.index(game) for game in games])
y_onehot = to_categorical(y, num_classes=len(games))

MODEL_FILENAME = "game_recommender_model.keras" 

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

if __name__ == "__main__":
    user_input = input("Введите теги через запятую (например: шутер, зомби): ")
    game, conf = recommend_game(user_input)
    print(f"Рекомендуемая игра: {game} (уверенность: {conf:.2f})")