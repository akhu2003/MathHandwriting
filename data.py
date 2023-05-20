import tensorflow as tf
batch_size = 32
img_size = (45,45)


train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'MathSymbols',
    batch_size=batch_size,
    image_size=img_size,
    validation_split=0.2,
    seed = 123,
    subset='training'
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'MathSymbols',
    batch_size=batch_size,
    image_size=img_size,
    validation_split=0.2,
    seed = 123,
    subset='validation'
)

