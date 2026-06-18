import requests
import json

# Crear varios usuarios de prueba
usuarios = [
    {'nombres': 'Juan Perez', 'correo': 'juan@example.com', 'edad': 30, 'contrasena': 'pass123'},
    {'nombres': 'Maria Garcia', 'correo': 'maria@example.com', 'edad': 28, 'contrasena': 'pass123'},
    {'nombres': 'Carlos Lopez', 'correo': 'carlos@example.com', 'edad': 35, 'contrasena': 'pass123'},
    {'nombres': 'Ana Martinez', 'correo': 'ana@example.com', 'edad': 22, 'contrasena': 'pass123'},
    {'nombres': 'Pedro Rodriguez', 'correo': 'pedro@example.com', 'edad': 45, 'contrasena': 'pass123'}
]

print("Insertando usuarios...")
for usuario in usuarios:
    try:
        resp = requests.post('http://localhost:8080/api/v1/usuarios', json=usuario)
        print(f"Usuario {usuario['nombres']} creado (Status: {resp.status_code})")
    except Exception as e:
        print(f"Error creando usuario {usuario['nombres']}: {e}")

# Crear varios gastos de prueba
gastos = [
    {'descripcion': 'Almuerzo', 'monto': 50000, 'fecha': '2026-06-17'},
    {'descripcion': 'Transporte', 'monto': 15000, 'fecha': '2026-06-17'},
    {'descripcion': 'Cena', 'monto': 45000, 'fecha': '2026-06-18'},
    {'descripcion': 'Almuerzo', 'monto': 55000, 'fecha': '2026-06-18'},
    {'descripcion': 'Cafe', 'monto': 8000, 'fecha': '2026-06-19'}
]

print("\nInsertando gastos...")
for gasto in gastos:
    try:
        resp = requests.post('http://localhost:8080/api/v1/gastos', json=gasto)
        print(f"Gasto {gasto['descripcion']} creado (Status: {resp.status_code})")
    except Exception as e:
        print(f"Error creando gasto {gasto['descripcion']}: {e}")

print("\nDatos insertados correctamente!")

