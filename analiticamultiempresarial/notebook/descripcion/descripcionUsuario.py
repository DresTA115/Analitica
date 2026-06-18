#Rutina para consumir API CON PYTHON

import json
import os
import requests

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def consumir_api_usuarios():
    
    #1. Definir la url del API
    url="http://localhost:8080/api/v1/usuarios"

    try:
        #2. Establecer el metodo HTTP que quiero consumir (GET/POST/PUT/DELETE)
        respuesta=requests.get(url, timeout=5)

        #3. Esperar la respuesta
        respuesta.raise_for_status()

        #4. Verificar que la respuesta viene en JSON
        datos=respuesta.json()
        
        #5a. Si viene vacio, cargar desde archivo local
        if not datos or (isinstance(datos, list) and len(datos) == 0):
            raise Exception("API devolvio datos vacios")
        
        return datos
    except (requests.exceptions.RequestException, Exception):
        #5b. Si falla, cargar desde usuarios.json
        local_file = os.path.join(ROOT_DIR, "usuarios.json")
        if os.path.exists(local_file):
            with open(local_file, encoding="utf-8-sig") as f:
                return json.load(f)
        raise