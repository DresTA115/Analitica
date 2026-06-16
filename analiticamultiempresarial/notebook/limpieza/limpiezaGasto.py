#TAREA: IMPORTAR A PANDAS
import pandas as pd

#TAREA: CREAR UNA FUNCION limpiar_datos_gasto(data_frame_gasto):

def limpiar_datos_gasto(data_frame_gasto):

#limpiar la descripcion para verificar que sie s un string, que no tienes espacios y que esta en minuscula

    data_frame_gasto["descripcion"]=data_frame_gasto["descripcion"].astype("string").str.strip().str.lower()


#limpiar el id para verificar que si es numero y que es mayor que 0

    data_frame_gasto["id"]=pd.to_numeric(data_frame_gasto["id"])
    data_frame_gasto=data_frame_gasto[data_frame_gasto["id"]>0]

#limpiar el monto para verificar que si es un numero y que es mayor que 0

    data_frame_gasto["monto"]=pd.to_numeric(data_frame_gasto["monto"])
    data_frame_gasto=data_frame_gasto[data_frame_gasto["monto"]>0]

#verificar que la fecha si es una fecha

    data_frame_gasto["fecha"]=pd.to_datetime(data_frame_gasto["fecha"], errors='coerce')

#cada uno define que campos para usted de (id, monto, descripcion y fecha) son obligatorios y eliminar los registros que vengan vacios

    data_frame_gasto=data_frame_gasto.dropna(subset=['id', 'monto', 'descripcion', 'fecha'])

    return data_frame_gasto