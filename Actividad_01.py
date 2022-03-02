# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
#IMPORTACION DE LAS LIBRERIAS A UTILIZAR
import os


import math


cwd= os.getcwd()

lista_AS = []


def leer():
    lista_archivos = os.listdir(cwd)

    for archivo in lista_archivos:
        if archivo.endswith(".AS"):
            lista_AS.append(archivo)
   
    print("Se encontraron: ",len(lista_AS)," archivos .AS")
    print ("Ésta es la lista de archivos: \n" , lista_AS)
    return lista_AS
leer()

def obs():
    for mediciones in lista_AS:
        os.system("teqc -O.dec 30 +obs " + mediciones.split("_")[0] + ".o "+ mediciones)

    
obs()   


print("Este es un programa para conervertir coordenadas geocéntricas a coordenadas geodésicas")

CLARKE1866=(6378206.4,6356583.8)
GRS80=(6378137,6356752.314)
WGS84=(6378137,6356752.314) 

def intro_coor():
    x= float(input("Ingrese Coordenada X => "))
    y= float(input("Ingrese Coordenada Y => "))
    z= float(input("Ingrese Coordenada Z => "))
    print()
    return (x,y,z)


def menu_selec(x,y,z,CLARKE1866,GRS80,WGS84):
    print("Elipsoides para transformación: ")
    print("1 => CLARKE1866")
    print("2 => GRS80")
    print("3 => WGS84")
    print("4 => Salir del programa")
    selecc=input("Seleccione el elipsoide para la transformación => ")
    print()
    
    if selecc== "1":
        print("Has elegido el Elipsoide de referencia CLARKE1866")
        e= (math.sqrt(pow(CLARKE1866[0],2)-pow(CLARKE1866[1],2)))/CLARKE1866[0] 
        e_prim= (math.sqrt(pow(CLARKE1866[0],2)-pow(CLARKE1866[1],2)))/CLARKE1866[1] 
        p= math.sqrt(x**2+y**2)
        theta= math.atan((z*CLARKE1866[0])/(p*CLARKE1866[1]))
        phi= math.atan((z+(e_prim**2)*(CLARKE1866[1])*((math.sin(theta))**3))/((p)-(e**2)*(CLARKE1866[0])*(math.cos(theta))**3))
        N= CLARKE1866[0]/ (math.sqrt(1-(e**2)*(math.sin(phi))**2))
        h= (p/(math.cos(phi)))-N
        lamb= math.atan(y/x)       
        lamb_deg= (lamb*180)/math.pi
        phi_deg= (phi*180)/math.pi
        
                
        print("Coordenadas Geodésicas: ")
        print("ɸ =>",phi_deg)
        print("λ =>",lamb_deg)
        print("h =>",h)
        
        return (lamb_deg,phi_deg,h)
    
    elif selecc== "2":   
        print("Has elegido el Elipsoide de referencia GRS80")
        e= (math.sqrt(pow(GRS80[0],2)-pow(GRS80[1],2)))/GRS80[0] 
        e_prim= (math.sqrt(pow(GRS80[0],2)-pow(GRS80[1],2)))/GRS80[1]
        p= math.sqrt(x**2+y**2)
        theta= math.atan((z*GRS80[0])/(p*GRS80[1]))
        phi= math.atan((z+(e_prim**2)*(GRS80[1])*((math.sin(theta))**3))/((p)-(e**2)*(GRS80[0])*(math.cos(theta))**3))
        N= GRS80[0]/ (math.sqrt(1-(e**2)*(math.sin(phi))**2))
        h= (p/(math.cos(phi)))-N
        lamb= math.atan(y/x)
        lamb_deg= (lamb*180)/math.pi
        phi_deg= (phi*180)/math.pi
        
        print("Coordenadas Geodésicas: ")
        print("ɸ =>",phi_deg)
        print("λ =>",lamb_deg)
        print("h =>",h)
        
        return (lamb_deg,phi_deg,h)
        
    elif selecc== "3":
        print("Has elegido el elipsoide de referencia WGS84")
        e= (math.sqrt(pow(WGS84[0],2)-pow(WGS84[1],2)))/WGS84[0] 
        e_prim= (math.sqrt(pow(WGS84[0],2)-pow(WGS84[1],2)))/WGS84[1] 
        p= math.sqrt(x**2+y**2)
        theta= math.atan((z*WGS84[0])/(p*WGS84[1]))
        phi= math.atan((z+(e_prim**2)*(WGS84[1])*((math.sin(theta))**3))/((p)-(e**2)*(WGS84[0])*(math.cos(theta))**3))
        N= WGS84[0]/ (math.sqrt(1-(e**2)*(math.sin(phi))**2))
        h= (p/(math.cos(phi)))-N
        lamb= math.atan(y/x)
        lamb_deg= (lamb*180)/math.pi
        phi_deg= (phi*180)/math.pi
        
        print("Coordenadas Geodésicas: ")
        print("ɸ =>",phi_deg)
        print("λ =>",lamb_deg)
        print("h =>",h)
        
        return (lamb_deg,phi_deg,h)
        
    elif selecc=="4":
        print("Programa finalizado")
        
(x,y,z)=intro_coor()
menu_selec(x,y,z,CLARKE1866,GRS80,WGS84)


