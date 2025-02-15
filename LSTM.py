import numpy as np
from pathlib import Path
from FastText import FastText
from keras.api.models import Sequential, load_model
from keras.api.layers import Embedding, LSTM, Dense, TimeDistributed
from keras.api.optimizers import Adam
from keras.api.callbacks import ReduceLROnPlateau

class ModeloLSTM():
    NOM_ARCHIVO = './data/modelo_lstm.h5'
    
    def __init__(
        self, 
        factor_aprendizaje:float = 0.002, 
        dim_embedding:int = 100, 
        unidades:int = 128, 
        tam_lote:int = 32, 
        validacion:float = 0.2, 
        fasttext:FastText = None
    ):
        self.FACTOR_APRENDIZAJE = factor_aprendizaje
        self.DIMENSION_EMBEDDING = dim_embedding
        self.UNIDADES = unidades
        self.TAM_LOTE = tam_lote
        self.VALIDACION = validacion
        self.fasttext = fasttext
    
    def construirModelo(self, tam_vocabulario_entrada = 0, max_tam_entrada = 0, tam_vocabulario_salida = 0):
        ruta = Path(self.NOM_ARCHIVO)
        if(ruta.is_file()):
            self.model = load_model(self.NOM_ARCHIVO)
            return True
        else:
            self.model = Sequential()
            self.model.add(
                Embedding(
                    input_dim=tam_vocabulario_entrada, 
                    output_dim=self.DIMENSION_EMBEDDING, 
                    input_length=max_tam_entrada,
                    weights=[self.fasttext.obtenerMatrizEmbedding('pregunta')],
                    trainable=False,
                )
            )
            self.model.add(LSTM(self.UNIDADES, return_sequences=True))
            self.model.add(Dense(tam_vocabulario_salida, activation='softmax'))
            self.model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(learning_rate=self.FACTOR_APRENDIZAJE))
            return False
        
    def entrenar(self, X:np.ndarray, y:np.ndarray, epocas:int = 50):
        res = self.model.fit(
            X, y, 
            batch_size=self.TAM_LOTE, 
            epochs=epocas, 
            validation_split=self.VALIDACION
        )
        self.model.save(self.NOM_ARCHIVO)
        return res
        
    def predeccir(self, x:str):
        prediccion = self.model.predict(x)
        return np.argmax(prediccion, axis=-1)[0]