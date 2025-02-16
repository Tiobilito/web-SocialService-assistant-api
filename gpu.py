import tensorflow as tf

# Verificar si TensorFlow puede acceder a la GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"GPUs detectadas: {len(gpus)}")
    for gpu in gpus:
        print(f" - {gpu}")
else:
    print("No se detectaron GPUs")