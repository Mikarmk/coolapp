import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

def tokenize(text_data, num_words=None):
    tokenizer = Tokenizer(num_words=num_words)
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
    predictors, label = input_sequences[:,:-1], input_sequences[:,-1]
    label = to_categorical(label, num_classes=total_words)
    return predictors, label

def build_model(total_words, max_sequence_length, embedding_dim=100, lstm_units=150):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(total_words, embedding_dim, input_length=max_sequence_length - 1),
        tf.keras.layers.LSTM(lstm_units, return_sequences=True),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.LSTM(lstm_units),
        tf.keras.layers.Dense(total_words, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def train_model(X, y, model, epochs=100):
    model.fit(X, y, epochs=epochs, verbose=1)

def generate_text(seed_text, next_words, model, tokenizer, max_sequence_length):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_length - 1, padding='pre')
        predicted_probs = model.predict(token_list)
        predicted_index = np.argmax(predicted_probs, axis=-1)[0]
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted_index:
                output_word = word
                break
        seed_text += " " + (output_word or "UNK")  # "UNK" is for unknown words
    return seed_text

# Теперь можешь использовать этот код для твоих нужд, предоставив данные в text_data.
