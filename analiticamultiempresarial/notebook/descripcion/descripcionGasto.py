#tarea: implementar funcion para consumir api gasto

import json
import os
import requests

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def consumir_api_gastos():

    url="http://localhost:8080/api/v1/gastos"

    try:
        respuesta=requests.get(url, timeout=5)
        respuesta.raise_for_status()
        datos=respuesta.json()
        
        if not datos or (isinstance(datos, list) and len(datos) == 0):
            raise Exception("API devolvio datos vacios")
        
        return datos
    except (requests.exceptions.RequestException, Exception):
        local_file = os.path.join(ROOT_DIR, "gastos.json")
        if os.path.exists(local_file):
            with open(local_file, encoding="utf-8-sig") as f:
                return json.load(f)
        raise