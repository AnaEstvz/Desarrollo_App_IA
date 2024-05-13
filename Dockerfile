# Utilizamos imagen phyton como base
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

RUN mkdir /src
#Establecemos el directorio de trabajo del contenedor
WORKDIR /src

#Copiar los archivos a ese directorio (COPY), que tambien vale APP
ADD . /src
#Instalar las dependencias 
RUN pip install -r requirements.txt

#Comando para ejecutar la app cuando el contenedor se inicializa 
CMD ["python", "fast_api.py"]
#Exponemos el puerto donde se va a ejecutar la app
EXPOSE 8000

