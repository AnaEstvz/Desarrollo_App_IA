from fastapi import FastAPI, HTTPException
import pickle
import uvicorn
import sqlite3
import pandas as pd
from cred import openai_key

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="template")

# Inicializa el modelo de lenguaje
llm = ChatOpenAI(api_key=openai_key)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/recomendacion')
async def recomendacion(zona: str):
    # Define el prompt base 
    prompt_template = PromptTemplate.from_template(
        "Recomiéndame una ruta de senderismo por la zona de {zona}."
    )

    # Define el rol del usuario en el prompt
    prompt_usuario = {"role": "user", "content": prompt_template.format(zona=zona)}

    # Realiza la llamada al modelo de lenguaje con el prompt completo
    respuesta = llm.invoke([{"role": "system", "content": "Eres un experto en senderismo, con un amplio conocimiento de las rutas por España, como la dificultad de la ruta, la duración, la distancia, la altitud y los puntos de interés. Sabes recomensar a la perfección lo que pide el usuario, pero solo sabes de senderismo, si te preguntan por otra cosa, debes responder amablemente que no estás entrenado para eso. Además la respuesta no debe ser extensa, menos de 150 palabras. Por favor, recomienda una ruta de senderismo significativa en la zona de "}, prompt_usuario])

    # Devuelve la respuesta generada por el modelo
    return HTMLResponse(content=respuesta.content)


@app.post('/guardar')
async def guardar_respuesta(data:dict):
    prompt_usuario = data.get("prompt_usuario")
    respuesta = data.get("respuesta")

    conn = sqlite3.connect("recomendacion.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS respuestas
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, prompt_usuario TEXT, respuesta TEXT)''')

    cursor.execute("INSERT INTO respuestas (prompt_usuario,respuesta) VALUES (?, ?)", (prompt_usuario, respuesta))

    conn.commit()
    conn.close()

    return {"mensaje": "Recomendaciones guardadas con éxito"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)














