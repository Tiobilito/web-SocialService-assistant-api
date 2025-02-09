# web-SocialService-assistant-api

Crea tu entorno virtual con (aunque puede no ser necesario):

```shell
python -m venv <nombre_del_entorno>
```

Activa tu entorno virtual en Windows con:

```shell
<nombre_del_entorno>\Scripts\activate
```

Puede haber errores al iniciar el entorno en Windows. Si ocurre, puedes ejecutar el siguiente comando (en PowerShell ejecutado como administrador):

```shell
Set-ExecutionPolicy RemoteSigned
```

Para revertir dicha acción, ejecuta:

```shell
Set-ExecutionPolicy Restricted
```

Instala los paquetes de `requirements.txt`:

```shell
pip install -r ./requirements.txt
```

A partir de aquí ya puedes instalar paquetes normalmente con **pip**.

### NOTAS:

1. Instala `keras`, `keras_preprocessing` y `tensorflow` para evitar fallos:

```shell
pip freeze > requirements.txt
```

2. Para salir del entorno virtual, ejecuta:

```shell
deactivate
```

### Entrenar el modelo

Para entrenar el modelo con tus propios datos, sigue estos pasos:

1. Abre el archivo `dataset.xlsx` en la carpeta `data`.
2. Reemplaza las columnas `USUARIO` y `ASISTENTE` con tus propias preguntas y respuestas.
3. Borra todos los archivos en la carpeta `data` excepto `dataset.xlsx`.
4. Ejecuta el script de la API para que el modelo se entrene automáticamente si no existen los archivos necesarios:

```shell
cd api
python api.py
```

Esto entrenará el modelo con tus datos y generará los archivos necesarios en la carpeta `data`.

### Ejecutar la API

Para ejecutar la API, navega al directorio api y ejecuta el archivo api.py:

```shell
cd api
python api.py
```

### Probar la API

Para probar la API desde el navegador, puedes utilizar la siguiente URL:

```
http://localhost:5000/pregunta?message=tu_pregunta
```

Reemplaza `tu_pregunta` con la pregunta que deseas enviar al modelo. La respuesta del modelo se mostrará en formato JSON en el navegador.
