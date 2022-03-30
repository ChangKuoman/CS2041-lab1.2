import pandas as pd
import numpy as np
from datetime import datetime

driver = pd.read_csv("driver.csv", delimiter=',')
service = pd.read_csv("service.csv", delimiter=',')

#ELIMINANDO ESPACIOS EN BLANCO
driver['Name'] = driver['Name'].apply(lambda x: x.strip())
driver['Base_Name'] = driver['Base_Name'].apply(lambda x: x.strip())
driver['Base_Website'] = driver['Base_Website'].apply(lambda x: x.strip())
driver['Base_Address'] = driver['Base_Address'].apply(lambda x: x.strip())
driver['Vehicle_License_Number'] = driver['Vehicle_License_Number'].apply(lambda x: x.strip())
driver['Active'] = driver['Active'].apply(lambda x: x.strip())
service['Vehicle_License_Number'] = service['Vehicle_License_Number'].apply(lambda x: x.strip())

print("\n---Ejercicio 1---\n")

# C1. ¿Cuales son los servicios de taxi que realiz ́o Paulino Ramon?
VLN = driver[driver["Name"]=="PAULINO,RAMON"]["Vehicle_License_Number"].values[0].strip()
print(service[service['Vehicle_License_Number']==VLN])

print("\n---Ejercicio 2---\n")

# C2. ¿Cuáles son los choferes que hicieron la mayor cantidad de servicios de taxi? Cruce la información de ambos archivos para obtener los resultados requeridos. Orden de mayor a menor y reportar el Top 10
placas = service['Vehicle_License_Number'].value_counts().head(10)
for i in range(0,10):
  print(driver[driver["Vehicle_License_Number"]==placas.index[i]]["Name"].values[0],
        " -> ",
        service[service["Vehicle_License_Number"]==placas.index[i]]["Vehicle_License_Number"].count())

print("\n---Ejercicio 3---\n")

# C3. ¿Algún chofer No Activo realiz ́o servicios de taxi?. Reporte los choferes inactivos y la cantidad de servicios realizados

PlacasDeChoferesNoActivos = driver[driver["Active"]=="NO"]["Vehicle_License_Number"].values
for i in PlacasDeChoferesNoActivos:
  cantidad = service[service["Vehicle_License_Number"]==i]["Vehicle_License_Number"].count()
  if cantidad != 0:
    print(i, driver[driver["Vehicle_License_Number"]==i]["Name"].values[0], cantidad)

print("\n---Ejercicio 4---\n")

# C4. ¿Cuántas empresas de taxi han registrado servicios de taxi? Verifique cuantas empresas (Base Name) tienen al menos un servicio de taxi asociado.

basename = driver["Base_Name"].value_counts()
print(basename)

print("\n---Ejercicio 5---\n")

# C5. ¿Qué empresa(s) de taxi (Base Name) reportaron servicio(s) el día 28 de diciembre?

lista = []
for x in range(len(service["lpep_pickup_datetime"].values)):
    date = str(" ".join([i for i in service["lpep_pickup_datetime"].values[x].split()[0].split('/')]))
    format_date = datetime.strptime(date, "%d %m %Y")
    if format_date.day == 28 and format_date.month == 12:
        placa = service.iloc[[x]]["Vehicle_License_Number"].values[0]
        valor = driver[driver["Vehicle_License_Number"] == placa]["Base_Name"].values[0]
        if valor not in lista and valor != "":
            lista.append(valor)

for i in lista:
    print(i)


