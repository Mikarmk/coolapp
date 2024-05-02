import tensorflow as tf
from tensorflow.keras import layers, models
import os
import matplotlib.pyplot as plt

def build_generator():
    model = models.Sequential()

    model.add(layers.Dense(256, input_shape=(100,), use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(alpha=0.2))

    model.add(layers.Dense(8 * 8 * 256, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(alpha=0.2))

    model.add(layers.Reshape((8, 8, 256)))

    model.add(layers.Conv2DTranspose(128, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(alpha=0.2))

    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(alpha=0.2))

    model.add(layers.Conv2D(3, (5, 5), padding='same', activation='tanh'))

    return model

noise = tf.random.normal([1, 100])

generator = build_generator()
generated_image = generator(noise, training=False)

output_dir = 'generated_images'
os.makedirs(output_dir, exist_ok=True)

plt.imshow(generated_image[0])
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'generated_image.png'))
plt.show()
