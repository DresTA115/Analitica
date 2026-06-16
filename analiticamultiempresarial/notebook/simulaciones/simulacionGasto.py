#Rutina para simular la fuente de datos que almacena datos de los gastos

import random

def simular_gastos(numeroGastosASimular):
   #id
   #fecha "2026-05-06"
   #monto
   #descripcion
   fecha=["2026-05-06","2026-05-07","2026-05-08","2026-05-09","2026-05-10","2026-05-11","2026-05-12","2026-05-13","2026-05-14","2026-05-15"]
   monto=[100,200,300,400,500,600,700,800,900,1000]
   descripcion=["Compra de materiales","Pago de servicios","Gastos de viaje","Alquiler de oficina","Salarios","Publicidad","Mantenimiento","Suministros","Consultoría","Otros"]

   #TAREA: PROGRAME AQUI FUNCION GENERADORA DE GASTOS SIMULADOS

   simulaciones_gastos=[]
   for i in range(numeroGastosASimular):
       gasto_simulado={
           "id":random.randint(1,500),
           "fecha":random.choice(fecha),
           "monto":random.choice(monto),
           "descripcion":random.choice(descripcion)
       }

#TAREA: PROGRAMAR RUTINA PARA INYECTAR ERRORES CONTROLADOS EN LSO CAMPOS ID,FECHA,MONTO,DESCRIPCION

       probabilidadError=random.random()
       if probabilidadError<0.2:
           gasto_simulado["id"]=None
       elif probabilidadError<0.4:
           gasto_simulado["fecha"]=random.choice([None,"2026-15-10","2026-10-32"])
       elif probabilidadError<0.5:
           gasto_simulado["monto"]=random.choice([None,-100,1000000])
       elif probabilidadError<0.7:
           gasto_simulado["descripcion"]=random.choice([None," ","1234567890"])


       simulaciones_gastos.append(gasto_simulado)
   return simulaciones_gastos




