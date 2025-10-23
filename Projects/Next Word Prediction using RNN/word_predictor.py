# next_word_prediction.py

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# 1. Load text file
with open(
    r"D:\fsds\projects\Next Word Prediction using RNN\Dataset\1661-0.txt",
    "r",
    encoding="utf-8",
) as f:
    text = f.read()

# 2. Tokenize the text
words = text.split()

tokenizer = Tokenizer()
tokenizer.fit_on_texts(words)

total_words = len(tokenizer.word_index) + 1
print("Total words:", total_words)

# 3. Generate input sequences
input_sequences = []
for i in range(1, len(words)):
    n_gram_sequence = words[: i + 1]
    token_list = tokenizer.texts_to_sequences([" ".join(n_gram_sequence)])[0]
    input_sequences.append(token_list)

# Pad sequences
max_seq_len = max([len(x) for x in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_seq_len, padding="pre")

predictors, label = input_sequences[:, :-1], input_sequences[:, -1]
label = to_categorical(label, num_classes=total_words)

# 4. Build the model
model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_seq_len - 1))
model.add(LSTM(150))
model.add(Dropout(0.2))
model.add(Dense(total_words, activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
print(model.summary())

# 5. Train the model
history = model.fit(predictors, label, epochs=50, verbose=1)


# 6. Function to predict next words
def predict_next_word(seed_text, next_words=5):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_seq_len - 1, padding="pre")
        predicted = np.argmax(model.predict(token_list, verbose=0), axis=-1)[0]

        for word, index in tokenizer.word_index.items():
            if index == predicted:
                seed_text += " " + word
                break
    return seed_text


# Example usage
print(predict_next_word("Once upon a time", next_words=5))
