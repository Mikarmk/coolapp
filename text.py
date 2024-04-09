import tensorflow as tf
from transformers import TFBartForConditionalGeneration, TFBartModel, BartTokenizerFast
import re
import random
import string

# Load the pre-trained BART model and tokenizer
model = TFBartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizerFast.from_pretrained('facebook/bart-large-cnn')

# Define a function to preprocess the text
def preprocess_text(text):
    text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text.lower())
    text = re.sub(r'\s+', ' ', text.strip())
    return text

# Load the dataset
def load_dataset(file_path):
    texts = []
    summaries = []
    with open(file_path, 'r') as file:
        for line in file:
            text, summary = line.strip().split('\t')
            texts.append(preprocess_text(text))
            summaries.append(preprocess_text(summary))
    return texts, summaries

# Prepare the dataset for training
def prepare_dataset(texts, summaries):
    tokenized_texts = tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors='tf')
    tokenized_summaries = tokenizer(summaries, padding=True, truncation=True, max_length=128, return_tensors='tf')
    return tokenized_texts, tokenized_summaries

# Train the model
def train(tokenized_texts, tokenized_summaries):
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    optimizer = tf.keras.optimizers.Adam(learning_rate=1e-5)
    model.compile(optimizer=optimizer, loss=loss)
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath='model_checkpoint', save_weights_only=True, save_best_only=True)
    model.fit(tokenized_texts, tokenized_summaries, epochs=3, callbacks=[checkpoint_callback])

# Generate a summary for a given text
def generate_summary(text):
    input_ids = tokenizer(text, return_tensors='tf', padding=True, truncation=True, max_length=512).input_ids
    summary = model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary[0])

# Main function
def main():
    file_path = 'path/to/your/dataset.txt'
    texts, summaries = load_dataset(file_path)
    tokenized_texts, tokenized_summaries = prepare_dataset(texts, summaries)
    train(tokenized_texts, tokenized_summaries)

if __name__ == '__main__':
    main()
