import requests

def test_recomendacion():
    # Prueba para la ruta de recomendación
    url = 'http://localhost:8000/recomendacion'
    zona = "Sierra Nevada"
    response = requests.get(url, params={'zona': zona})
    assert response.status_code == 200
    assert response.text

def test_guardar_respuesta():
    # Prueba para la ruta de guardar respuesta
    url = 'http://localhost:8000/guardar'
    data = {
        "prompt_usuario": "Recomiéndame una ruta de senderismo en Sierra de Guadarrama.",
        "respuesta": "Una ruta popular en Sierra de Guadarrama es la ruta de la Cuerda Larga. Tiene una duración de unas 6 horas y ofrece vistas impresionantes."
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Recomendaciones guardadas con éxito"}
