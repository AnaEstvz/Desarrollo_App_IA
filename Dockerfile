
#Dockerizamos la app para facilitar su despliegue y escalabilidad. Esto permite que no solo se ejecute en local, sino que otros usuarios puedan usarla
# Utilizamos Docker para empaquetar la aplicación y sus dependencias en un contenedor independiente.
# Aseguramos la portabilidad y la consistencia del entorno de ejecución de la aplicación.
# Imagen de Python 
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

RUN mkdir /src

WORKDIR /src

ADD . /src
#Instalar las dependencias 
RUN pip install -r requirements.txt

# Comandos para ejecutar la app cuando el contenedor se inicializa 
CMD ["python", "fast_api.py"]

# Puerto donde se va a ejecutar la app
EXPOSE 8000

