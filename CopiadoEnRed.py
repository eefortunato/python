# -*- coding: cp1252 -*-
#import PyPDF2 #Libreria para manejar PDF en PYTHON
#Creado por Eric Fortunato Version 1.0 25/04/2017
import os #Libreria de Sistema Operativo de PYTHON
from shutil import copytree #Libreria de python para operaciones de alto nivel en archivos y directorios como copiado y remocion/borrado
import logging #Libreria de python para llevar registro/bit�cora de errores

def obtenerRuta(carpeta, listaruta, ruta): #Funcion recursiva para obtener todas las rutas de un directorio
    rutaCompleta=ruta #variable que almacena la ruta al momento
    if os.path.isdir(carpeta): #Si es directorio continua hacia adentro
        subcarpetas=os.listdir(carpeta)
        for nuevodir in subcarpetas:
            rutaactual=carpeta+nuevodir+'\\'
            rutaCompleta+=nuevodir
            if os.path.isdir(rutaactual): #para cada subdirectorio continua adentrandose llamando a la funcion de manera recursiva
                rutaCompleta+='\\'
                obtenerRuta(rutaactual, listaruta, rutaCompleta)
            else: #si alguna de las carpetas resula ser un archivo y no hay mas subdirectorios se agrega a la lista de rutas
                listaruta.append(rutaCompleta)
            rutaCompleta=ruta
    else: #si la carpeta no es directorio inmediatamente la agrega a la lista de rutas
        archivos=os.listdir(carpeta)
        for archivo in archivos:
            listaruta.append(rutaCompleta+archivo)

def total_size(source): #funcion recursiva para calcula el peso en bytes del directorio
        pesototal = os.path.getsize(source)
        for item in os.listdir(source):
            itempath = os.path.join(source, item)
            if os.path.isfile(itempath):
                pesototal += os.path.getsize(itempath)
            elif os.path.isdir(itempath):
                pesototal += total_size(itempath)
        return pesototal

RUTA = '\\\\192.168.3.1\\d\\COLAS\\' #Ruta donde estan las colas
RUTA2= '\\\\192.168.3.1\\d\\DATABRUTA\\' #Ruta de DATABRUTA
RUTA3= '\\\\192.168.3.1\\d\\VOLUMENES\\' #Ruta de los volumenes

listarutaOrigen=[]
listarutaDestino=[]


DESTINO ='G:\\BackupVertia\\COLAS\\'
DESTINO2='G:\\BackupVertia\\DATABRUTA\\'
DESTINO3='G:\\BackupVertia\\VOLUMENES\\'
LOG_FILENAME = 'Errores.txt'

try:
    #esta funcion hace un recorrido de los directorios como si fueran arboles para copiar toda la estructura igual al origen
    copytree(RUTA,DESTINO,symlinks=False, ignore=None)
    copytree(RUTA2,DESTINO2,symlinks=False, ignore=None)
    copytree(RUTA3,DESTINO3,symlinks=False, ignore=None)
except Exception as inst: #Si se produce algun error se crea una bit�cora con los errores de copiado.
    print "Se produjo un error, se crear� archivo con los errores"
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    logging.debug(inst)


origenSize=0
origenSize2=0
origenSize3=0
destinoSize=0
destinoSize2=0
destinoSize3=0


rutaOrigen='\\'
rutaOrigen2='\\'
rutaOrigen3='\\'
rutaDestino='\\'
rutaDestino2='\\'
rutaDestino3='\\'

origenSize=total_size(RUTA)
origenSize2=total_size(RUTA2)
origenSize3=total_size(RUTA3)
destinoSize=total_size(DESTINO)
destinoSize2=total_size(DESTINO2)
destinoSize=total_size(DESTINO3)


obtenerRuta(RUTA, listarutaOrigen, rutaOrigen)
obtenerRuta(RUTA2, listarutaOrigen, rutaOrigen2)
obtenerRuta(RUTA3, listarutaOrigen, rutaOrigen3)

if origenSize == destinoSize:
    print "Tienen el mismo tamanio"

if origenSize2 == destinoSize2:
    print "Tienen el mismo tamanio"

if origenSize3 == destinoSize3:
    print "Tienen el mismo tamanio"

obtenerRuta(DESTINO, listarutaDestino, rutaDestino)
obtenerRuta(DESTINO2, listarutaDestino, rutaDestino2)
obtenerRuta(DESTINO3, listarutaDestino, rutaDestino3)

contadorRutas=0
for rutas in listarutaOrigen:
    if rutas in listarutaDestino:
        contadorRutas+=1

if len(listarutaOrigen)==contadorRutas:
    print "Tienen las mismas rutas"
