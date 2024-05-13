# Proyecto Final: Desarrollo de una Aplicación de IA Generativa

## Descripción del Proyecto:

En este proyecto final del módulo de Data Engineering, hemos desarrollado una aplicación web que permite a los usuarios interactuar con modelos de lenguaje (LLMs), integrada con Python y FastAPI. La aplicación registra las consultas y respuestas en una base de datos desplegada en Render para mantener un histórico de las interacciones.

## Objetivos:

- Desarrollar una aplicación web utilizando Python y FastAPI que permita a los usuarios interactuar con modelos de lenguaje.
- Integrar LLMs (ChatGPT, HuggingFace, etc.) para acceder a modelos pre-entrenados y realizar inferencias sobre texto, utilizando la funcionalidad de Langchain para mejorar la calidad de las respuestas generadas por el modelo.
- Implementar un sistema de registro en una base de datos desplegada en Render para almacenar un histórico de las interacciones de los usuarios.
- Dockerizar la aplicación para facilitar su despliegue y escalabilidad, así como subir todos los recursos a DockerHub y Github.

## Requisitos Técnicos:

1. **Desarrollo de la Aplicación Web:**
   - Utilizamos Python y FastAPI para construir la infraestructura de la aplicación.
   - Diseñamos endpoints que permiten a los usuarios enviar consultas a través de la API.
   - Desarrollamos el testeo del código y de los diferentes endpoints para asegurar su funcionamiento correcto.

2. **Integración con LLM:**
   - Elegimos integrar nuestra aplicación con OpenAI utilizando su API para acceder al modelo de lenguaje GPT-3.
   - Configuramos la API para enviar consultas a OpenAI y recibir respuestas generadas por el modelo.

3. **Uso de Langchain PromptTemplate:**
   - Implementamos la funcionalidad de PromptTemplate de Langchain para mejorar la coherencia y relevancia de las respuestas generadas por el modelo.
   - Esto nos permitió personalizar y estructurar mejor las consultas enviadas al modelo de lenguaje.

4. **Registro en Base de Datos:**
   - Configuramos una base de datos en AWS utilizando PostgreSQL para almacenar un registro histórico de las interacciones de los usuarios.
   - Diseñamos un esquema de base de datos simple pero adecuado para almacenar consultas y respuestas.

5. **Dockerización de la Aplicación:**
   - Utilizamos Docker para empaquetar nuestra aplicación y sus dependencias en un contenedor independiente.
   - Esto nos permitió garantizar la portabilidad y la consistencia del entorno de ejecución de nuestra aplicación.

6. **Despliegue y Distribución:**
   - Subimos la imagen de Docker resultante a DockerHub para que pueda ser fácilmente accesible y distribuida.
   - Subimos el código fuente de nuestra aplicación a GitHub junto con la documentación necesaria para su configuración, ejecución y mantenimiento.

## Despliegue en Render y Uso de OpenAI

La aplicación se encuentra desplegada en Render, un servicio de alojamiento en la nube, y utiliza la API de OpenAI para acceder al modelo de lenguaje GPT-3. A continuación, se detallan los pasos y consideraciones relevantes para el despliegue y el uso de OpenAI:

1. **Despliegue en Render:**
   - Render ofrece una plataforma de alojamiento en la nube fácil de usar que permite implementar aplicaciones de forma rápida y sencilla.
   - Para desplegar la aplicación en Render, configuramos un entorno de ejecución adecuado, definimos los archivos de configuración necesarios (como `Dockerfile` y `requirements.txt`) y seguimos los pasos proporcionados por Render para implementar la aplicación.

2. **Uso de OpenAI:**
   - OpenAI proporciona una API que permite acceder a modelos de lenguaje pre-entrenados, como GPT-3, para realizar inferencias sobre texto.
   - Para utilizar OpenAI en nuestra aplicación, nos registramos en la plataforma de OpenAI, obtenemos una clave de API y la utilizamos en nuestra aplicación para autenticar las solicitudes a la API de OpenAI.
   - Configuramos la API de nuestra aplicación para enviar consultas a OpenAI y recibir respuestas generadas por el modelo. Utilizamos la funcionalidad de Langchain PromptTemplate para mejorar la calidad y la coherencia de las respuestas generadas.

3. **Seguridad y Privacidad:**
   - Al utilizar servicios en la nube como Render y OpenAI, es importante considerar la seguridad y la privacidad de los datos. Nos aseguramos de implementar medidas de seguridad adecuadas, como el manejo seguro de credenciales y la protección contra vulnerabilidades conocidas.

4. **Escalabilidad y Mantenimiento:**
   - Render ofrece escalabilidad automática para manejar cargas de trabajo variables y garantizar un rendimiento óptimo de la aplicación.
   - Mantenemos nuestra aplicación actualizada y nos mantenemos al tanto de las actualizaciones y cambios en las API y servicios que utilizamos, como OpenAI, para garantizar su funcionamiento continuo y óptimo.

Con estos pasos, logramos desplegar nuestra aplicación en Render y utilizar OpenAI para proporcionar respuestas generadas por un modelo de lenguaje avanzado como GPT-3. Esto nos permite ofrecer una experiencia de usuario mejorada y respuestas más relevantes y coherentes a las consultas de los usuarios.


## Uso de la Aplicación

Para utilizar esta aplicación, necesitarás lo siguiente:

- Una API Key de OpenAI para acceder a la API de generación de lenguaje.
- Una URL de base de datos en Render para almacenar el registro de interacciones de los usuarios.

### Clona el Repositorio:
git clone https://github.com/AnaEstvz/Desarrollo_App_IA.git

### Configura las Variables de Entorno:
Crea un archivo .env en el directorio raíz del proyecto y define las siguientes variables de entorno:

- OPENAI_API_KEY=your_openai_api_key
- DATABASE_URL=your_render_database_ur

### Construye la Imagen de Docker:

docker build -t nombre_imagen 

### Ejecuta el Contenedor Docker:
docker run -d -p 8000:8000 nombre_image

### Accede a la Aplicación:
Abre un navegador web y visita http://localhost:8000 para acceder a la aplicación.