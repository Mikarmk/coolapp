import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def tokenize(text_data):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(text_data)
    total_words = len(tokenizer.word_index) + 1
    return tokenizer, total_words

def preprocess_data(text_data, tokenizer, max_sequence_length):
    input_sequences = []
    for line in text_data:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)
    input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length, padding='pre')
    X, y = input_sequences[:,:-1],input_sequences[:,-1]
    y = tf.keras.utils.to_categorical(y, num_classes=total_words)
    return X, y

def build_model(total_words, max_sequence_length):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Embedding(total_words, 100, input_length=max_sequence_length-1))
    model.add(tf.keras.layers.LSTM(150))
    model.add(tf.keras.layers.Dense(total_words, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def train_model(X, y, model, epochs):
    model.fit(X, y, epochs=epochs, verbose=1)

def generate_text(seed_text, next_words, model, tokenizer, max_sequence_length):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_length-1, padding='pre')
        predicted = model.predict_classes(token_list, verbose=0)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

text_data = [
    "The quick brown fox jumps over the lazy dog",
    "She sells seashells by the seashore"
]

tokenizer, total_words = tokenize(text_data)
max_sequence_length = 10
X, y = preprocess_data(text_data, tokenizer, max_sequence_length)

model = build_model(total_words, max_sequence_length)
train_model(X, y, model, epochs=100)

seed_text = "brown fox"
next_words = 5
generated_text = generate_text(seed_text, next_words, model, tokenizer, max_sequence_length)
print(generated_text)
