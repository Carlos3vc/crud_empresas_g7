import csv
import os

ARCHIVO_CSV = 'empresas.csv'

def cargar_empresas():
    empresas = {}

    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                ruc = fila["ruc"]
                empresas[ruc] = {
                    "razon_social": fila["razon_social"],
                    "direccion": fila["direccion"]
                }

    return empresas

def guardar_empresas(empresas):
    with open(ARCHIVO_CSV, mode="w", encoding="utf-8", newline="") as archivo:
        campos = ["ruc", "razon_social", "direcion"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        for ruc, info in empresas.items():
            escritor.writerow({
                "ruc": ruc,
                "razon_social": info["razon_social"],
                "direccion": info["direccion"]
            })

empresas = cargar_empresas()