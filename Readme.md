# Ejemplo de aplicacin Flask con gunicorn para desplegar en Heroku

Aplicacion mínima Flask para desplegar en la plataforma Heroku. 

Siguiendo los pasos del articulo: https://www.rqlogic.com/flask-en-entorno-de-produccion-con-gunicorn/

Se pretende tener configuraciones separadas segun el entorno en donde se despliegue la aplicacion.

## Preparacion de la aplicacion en local

### Creacion del entorno virtual

Creamos un entorno virtual independiente para la aplicación. 

En la carpeta de la aplicacion ejecutamos:

    virtualenv env

### Variables de entorno

Para la aplicacion funcione creamos las siguientes variables de entorno:

#### Linux/Mac

    export FLASK_APP="wsgi"
    export FLASK_ENV="development"
    export APP_SETTINGS_MODULE="config.local"

#### Windows

    set "FLASK_APP=wsgi"
    set "FLASK_ENV=development"
    set "APP_SETTINGS_MODULE=config.local"
    
Es recomendable añadir las variables en el fichero "activate" o "activate.bat" del entorno virtual creado. 

### Activacion del entorno virtual

Desde la consola ejecutamos:

    source ./env/Scripts/activate

### Desactivacion del entorno virtual

Desde la consola ejecutamos:

    deactivate

### Instalación de dependencias

En el proyecto se distribuye un fichero (requirements.txt) con todas las dependencias. Para instalarlas
basta con ejectuar:

    pip install -r requirements.txt

### Ejecución con el servidor que trae Flask

Una vez descargado el proyecto, creado las variables de entorno e instalado las dependencias,
para arrancar el proyecto ejecutaremos:

    flask run

### Ejecucion desde el servidor de aplicaciones gunicorn

    gunicorn --bind 0.0.0.0:5000 wsgi:app


## Puesta en produccion [heroku]

1. Instalar Heroku Command Line Interface (CLI) https://devcenter.heroku.com/articles/getting-started-with-python#set-up

2. Logearse con el cliente en heroku 
    heroku login

3. Clonar o preparar el repositorio git local a vincular con heroku

    Procfile, runtime.txt y requirements.txt
    pip freeze > requirements.txt

4. Crear la aplicacion 
    heroku create hola-heroku-200719
    
Creating hola-heroku-200719... done
https://hola-heroku-200719.herokuapp.com/ | https://git.heroku.com/hola-heroku-200719.git

    heroku config:set FLASK_APP=wsgi
    heroku config:set FLASK_ENV=production
    heroku config:set APP_SETTINGS_MODULE=config.prod

5. Subir los cambios al repositorio remoto de la app en heroku

    git push heroku master

