from time import sleep
from src.datos import empresas,guardar_empresas
from src.utils import pausa,titulo,limpiar
from src.decoradores import pantalla

@pantalla("REGISTRAR EMPRESA")
def registrar_empresas():
    ruc = input("INGRESE RUC : ")
    razon_social = input("INGRESE RAZON SOCIAL : ")
    direccion = input("INGRESE DIRECCION : ")
    
    empresas[ruc] = {
        "razon_social":razon_social,
        "direccion":direccion
    }
    titulo("EMPRESA REGISTRADO EXITOSAMENTE!!!")
    
@pantalla("MOSTRAR EMPRESAS")
def mostrar_empresas():
    for ruc,info in empresas.items():
        print(f"RUC : {ruc}")
        print(f"RAZON SOCIAL : {info['razon_social']}")
        print(f"DIRECCION : {info['direccion']}")
        print("*" * 50)
        
@pantalla("ACTUALIZAR EMPRESAS")
def actualizar_empresas():
    ruc = input("INGRESE RUC DE LA EMPRESA A ACTUALIZAR : ")

    if ruc in empresas:
        print(f"EMPRESA ENCONTRADA : {empresas[ruc]['razon_social']}")
        print("INGRESAR NUEVOS DATOS O PRESIONAR ENTER PARA CONSERVARLOS")

        nuevo_razon_social = input(f"NUEVA RAZON SOCIAL ({empresas[ruc]['razon_social']}): ")
        nuevo_direccion = input(f"NUEVA DIRECCION ({empresas[ruc]['direccion']}): ")

            
        empresas[ruc]["razon_social"] = nuevo_razon_social if nuevo_razon_social else empresas[ruc]["razon_social"]

        if nuevo_direccion!= "":
            empresas[ruc]["direccion"] = nuevo_direccion

        print("ACTUALIZANDO EMPRESA...")
    else:
        print("EMPRESA NO ENCONTRADA...")
        
@pantalla("ELIMINAR EMPRESA")
def eliminar_empresa():
    ruc = input("INGRESE RUC DE EMPRESA A ELIMINAR : ")

    if ruc in empresas:
        del empresas[ruc]
        print("REGISTRO DE EMPRESA ELIMINADA")
    else:
        print("EMPRESA NO ENCONTRADA...")
        
def menu_principal():
    while True:
        limpiar()
        titulo("CRUD DE EMPRESAS")
        print("""
            [1] REGISTRAR EMPRESAS
            [2] MOSTRAR EMPRESAS
            [3] ACTUALIZAR EMPRESAS
            [4] ELIMINAR EMPRESAS
            [5] SALIR
        """)
        
        opcion = int(input("INGRESE OPCIÓN : "))
        
        if opcion == 1:
            registrar_empresas()
            pausa()
        elif opcion == 2:
            mostrar_empresas()
            pausa()
        elif opcion == 3:
            actualizar_empresas()
            pausa()
        elif opcion == 4:
            eliminar_empresa()
            pausa()
        elif opcion == 5:
            guardar_empresas(empresas)
            limpiar()
            titulo("SALIENDO DEL SISTEMA...")
            print("DATOS GUARDADOS EN empresas.csv")
            sleep(2)
            break
        else:
            print("OPCIÒN NO VALIDA.")