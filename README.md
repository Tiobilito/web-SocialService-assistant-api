# web-SocialService-assistant-api

Crea tu entorno virtual con (aunque puede no ser necesario):

```shell
python -m venv venv
```

Activa tu entorno virtual en Windows con:

```shell
venv\Scripts\activate
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
