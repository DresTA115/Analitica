#tarea: implementar funcion para consumir api gasto

import requests

def consumir_api_gastos():

    url="http://localhost:8080/api/gastos"

    respuesta=requests.get(url)

    respuesta.raise_for_status()

    datos=respuesta.json()

    return datos