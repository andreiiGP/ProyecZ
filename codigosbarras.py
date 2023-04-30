#@creador Andrei 
# importate instalar el componente pip install python-barcode y para que los ponga en png  pip install pillow
import os  #para limpiar pantalla
from PIL import Image # cudrar imagen de el cb 
import time # tiempo en pantalla
import barcode  # se importa la bibloteca
# de la biblioteca barcode traemos el componente para generar imagenes
from barcode.writer import ImageWriter

def generarCodigo():  # funcion generar codigo

    nombreC = input("ingrese el nombre de la careta para guardar los codigos :")
    if not os.path.exists(nombreC): # si no exite la carpeta en donde se corre el codigo se crea una 
        os.makedirs(nombreC)

    cantidadCodigos = int(input("Ingrese la cantidad de codigos que desea realizar : ")) # se le pide al ususario cuantos cb quere realizar
    os.system("cls")# se limpia pantalla
    for i in range(0, cantidadCodigos): # ciclo for repite para generar los cb segun el numero ingresado por el usuario
        caracter = (input(f"Ingrese Los caracteres para crear su codigo : "))
        formato_barcode = barcode.get_barcode_class('code128') #formato del codigo se puede cambiar a ean13 o X formato
        codigo = formato_barcode(caracter, writer=ImageWriter()) #Genera el cb 
        codigo.save(f"{nombreC}/{nombreC} {i}") # guarda el cb

        logo = Image.open("logo/logosentryo.png")# abre el cb
        codigo_imagen = Image.open(f"{nombreC}/{nombreC} {i}.png")#copia el cb ya guarado lo abre
        nuevo_codigo_imagen = Image.new("RGB", (int(codigo_imagen.size[0]*1), int(codigo_imagen.size[1]*1.2)), (255, 255, 255))#lo pega redimencionado 
        nuevo_codigo_imagen.paste(codigo_imagen, (0, 70))# valores para colocar el cb

        ancho_logo, alto_logo = logo.size # establecemos el ancho del logo
        ancho_codigo, alto_codigo = codigo_imagen.size #  ajustar el tamaño y la posición de los elementos en la imagen final.
        posicion_x = int((ancho_codigo - ancho_logo) / 2)#  calculamos la posición horizontal en la que se debe pegar el logo en la imagen final
        posicion_y = 5 # establecemos la posición vertical en la que se debe pegar el logo 
        nuevo_codigo_imagen.paste(logo, (posicion_x, posicion_y), logo)# pegamos la imagen en el logo final
        nuevo_codigo_imagen.save(f"{nombreC}/{nombreC} {i}.png") # lo guarda denuevo con el logo colocado sobrescribiendolo
    os.system("cls") #limpiamos pantalla
    print("codigos generados correctamente") # mensaje al usuario
    time.sleep(1)# esperamos 1 segundo 
    os.system("cls") # limpiamos pantalla 
    GenerarCB()# redirigimoa l menu principal

def GenerarCB():  # funcion usuario
    while True:
        print('MENU DE OPCIONES')
        print("1°:Geneara CB")
        print("2°:Salir")
        print("-----------------")
        op =(input("Su Opcion : "))
        if op == "1":
            os.system("cls")
            generarCodigo()
            break
        elif op == "2":
            print("Vuelva Pronto")
            time.sleep(1)  
            break
        else:
            print("ingrese una opcion correcta")
            time.sleep(1) 
            os.system("cls")
            
GenerarCB()