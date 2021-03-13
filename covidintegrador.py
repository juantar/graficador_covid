# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 00:06:10 2020

@author: Jotaté
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import requests

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget("https://covid.ourworldindata.org/data/ecdc/full_data.csv'")



df = pd.read_csv("full_data.csv")
df.date = pd.to_datetime(df.date)



paises= []
crucex = [] #Cruce para casos totales en el eje x
crucey = [] #Cruce para casos totales en el eje y

p1x = [] #Variables utilizadas para casos totales
p2x = []
p1y = []
p2y = []

crucexx = [] #Cruce para muertes totales en el eje x
cruceyy = [] #Cruce para muertes totales en el eje y

p11x = [] #Variables utilizadas para muertes totales
p22x = []
p11y = []
p22y = []


def graficador (pais):
    plt.plot(df.date[(df.location == pais)] , df.total_cases[(df.location == pais)],label="Casos totales en {}" .format(pais))
    plt.plot(df.date[(df.location == pais)] , df.total_deaths[(df.location == pais)],label="Muertos totales en {}" .format(pais))                 
    plt.xticks(rotation = 45) 
    plt.title(pais)
    plt.xlabel('Fecha')
    plt.ylabel('Casos/Muertes')
    plt.tight_layout()
    plt.legend()
    plt.grid(b=True, axis="both") 
    plt.show(block=False)



def comparador_graf ():
    for pais in paises:        
        plt.plot(df.date[(df.location == pais) & (df.date > fecha_inicial) & (df.date < fecha_final)] , 
                 df.total_deaths[(df.location == pais)& (df.date > fecha_inicial) & (df.date < fecha_final)],label="Muertos totales en {}".format(pais))   
        plt.plot(df.date[(df.location == pais) & (df.date > fecha_inicial) & (df.date < fecha_final)] ,
                 df.total_cases[(df.location == pais)& (df.date > fecha_inicial) & (df.date < fecha_final)],label="Casos totales en {}".format(pais))
        plt.title("Comparación entre{}" .format(paises))
        plt.xlabel('Fecha')
        plt.ylabel('Casos/Muertes')
        plt.tight_layout()
        plt.legend()
        plt.grid(b=True, axis="both")
        plt.xticks(rotation = 45)
        plt.xlim(pd.to_datetime(fecha_inicial),pd.to_datetime(fecha_final))
        interseccion_totalcases()
        interseccion_totaldeaths()
    plt.show(block=False)  
    return


def interseccion_totalcases():
   for i,k,l,m in zip(df.date[df.location == paises[0]],df.date[df.location == paises[1]],df.total_cases[df.location == paises[0]],df.total_cases[df.location == paises[1]]):  
    p1y.append(l)
    p2y.append(m)
    p1x.append(i)
    p2x.append(k)
   for i in  range(len(p1y)):
       
       if (p1y[i] == p2y[i]) or (p1y[i] > p2y[i] and p1y[i-1] < p2y[i-1]) or (p1y[i] < p2y[i] and p1y[i-1] > p2y[i-1]):     
           crucex.append(p1x[i])
           crucey.append(p1y[i])
      
   plt.scatter(crucex, crucey, s=100, edgecolor="k", facecolor=None)


def interseccion_totaldeaths():
   for i,k,l,m in zip(df.date[df.location == paises[0]],df.date[df.location == paises[1]],df.total_deaths[df.location == paises[0]],df.total_deaths[df.location == paises[1]]):  
    p11y.append(l)
    p22y.append(m)
    p11x.append(i)
    p22x.append(k)
   for i in  range(len(p11y)):
       
       if (p11y[i] == p22y[i]) or (p11y[i] > p22y[i] and p11y[i-1] < p22y[i-1]) or (p11y[i] < p22y[i] and p11y[i-1] > p22y[i-1]):     
           crucex.append(p11x[i])
           crucey.append(p11y[i])
      
   plt.scatter(crucexx, cruceyy, s=100, edgecolor="g", facecolor=None)



def logaritmo():
    for pais in paises:
                plt.plot(df.date[(df.location == pais) & (df.date > fecha_inicial) & (df.date < fecha_final)] ,
                 df.total_cases[(df.location == pais)& (df.date > fecha_inicial) & (df.date < fecha_final)],label="Casos totales en {}".format(pais))
                plt.plot(df.date[(df.location == pais)& (df.date > fecha_inicial) & (df.date < fecha_final)] , 
                 df.total_deaths[(df.location == pais)& (df.date > fecha_inicial) & (df.date < fecha_final)],label="Muertos totales en {}".format(pais))
                plt.yscale('log')
                plt.title("Comparación entre {} en escala logaritmica" .format(paises))
                plt.xlabel('Fecha')
                plt.ylabel('Casos/Muertes en escala log')
                # plt.tight_layout()
                plt.grid(b=True, axis="both")
                plt.legend()
                plt.xticks(rotation = 45)
                plt.xlim(pd.to_datetime(fecha_inicial),pd.to_datetime(fecha_final))
    plt.show(block=False) 
        
def verificador(pais):
    if pais not in df.location.values:
                print("El pais seleccionado no se encuentra, por favor ingrese uno nuevo")
                print("Recuerde que los mismos se encuentran en inglés y se debe incluir la letra mayúscula")
    else:
        paises.append(pais)
            
def verificador_fecha_inicial(fecha_inicial):
    try:
        datetime.datetime.strptime(fecha_inicial, '%Y-%m-%d')
        return  True
    except ValueError:
        return  False


def verificador_fecha_final(fecha_final):
    try:
        datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
        return  True
    except ValueError:
        return  False




def limpieza_listas ():
    paises.clear()
    crucex.clear()
    crucey.clear()
    p1x.clear()
    p2x.clear()
    p1y.clear()
    p2y.clear()
    crucexx.clear()
    cruceyy.clear()
    p11x.clear()
    p22x.clear()
    p11y.clear()
    p22y.clear()
    


def menu():
    print("Bienvenido al Graficador de casos del COVID-19.")
    print()
    print("Este programa permite:")
    print()
    print("1. Graficar los casos totales y muertes totales de un país en función del tiempo") 
    print()
    print("2. Comparar entre 2 paises casos totales y muertes totales en un intervalo de fechas y mostrar su intersección")
    print()
    print("3. Comparar entre n paises casos totales y muertes totales en un intervalo de fechas en escala logratimica")
    print()
    print("4. Salir")
    print()
    print("0. Ayuda")



def ayuda():
    print("Si el programa no da la opción de volver al menu, luego de mostrar un gráfico, pruebe cerrando el mismo. ")
    print()
    print("Los nombres de los paises se encuentran en inglés y con mayúscula. Esto se debe respetar.")
    print()
    print("Si aún así, no encuentra el país es posible que este no se encuentre en la base de datos.")
    print()
    print("Las información disponible se tiene desde febrero del 2020.")
    print()
    print("En la opción 3 si desea comparar los paises seleccione no cuando se le pregunta por agregar otro pais. ")
    




menu()
print()            
print()
seleccion = int(input("Por favor seleccione una opción de las 4 posibles:"))
while seleccion != 4:
    if seleccion == 0:
        print()
        print()
        ayuda()
        
    if seleccion == 1:
        print()
        print()
        pais = input("Ingrese un país: ")
        verificador(pais)
        graficador(pais)
        
    elif seleccion == 2:
        while len(paises) <= 1:
            print()
            print()
            pais = input("Ingrese un país: ")  
            verificador(pais)
        print()
        print()
        fecha_inicial = input("Ingrese fecha de inicio en formato YYYY-MM-DD:")
        verificador_fecha_inicial(fecha_inicial)            
        while verificador_fecha_inicial(fecha_inicial) == False:
            print()
            print()
            print("Ingreso una fecha incorrecta,revise, debería ser YYYY-MM-DD")
            print()
            print()
            fecha_inicial = input("Ingrese fecha de inicio en formato YYYY-MM-DD:")
            verificador_fecha_inicial(fecha_inicial)
        print()
        print()        
        fecha_final = input("Ingrese fecha final en formato YYYY-MM-DD:") 
        verificador_fecha_final(fecha_final)
            
        while verificador_fecha_final(fecha_final) == False:
            print()
            print()
            print("Ingreso una fecha incorrecta,revise, debería ser YYYY-MM-DD")
            print()
            print()
            fecha_final = input("Ingrese fecha final en formato YYYY-MM-DD:") 
            verificador_fecha_final(fecha_final)
 
        comparador_graf()
       
            
    elif seleccion == 3:
        print()
        print()
        pais = input("Ingrese un país: ")
        verificador(pais)
        print()
        print()
        pregunta = input("Desea ingresar otro país?(ingrese si/no):")
        while pregunta == "si":
            print()
            print()
            pais = input("Ingrese un país: ")
            verificador(pais)
            print()
            print()
            pregunta = input("Desea ingresar otro país? (ingrese si/no):")
            if pregunta == "no":
                print()
                print()
                fecha_inicial = input("Ingrese fecha de inicio en formato YYYY-MM-DD:")
                verificador_fecha_inicial(fecha_inicial)
                while verificador_fecha_inicial(fecha_inicial) == False:
                    print()
                    print()
                    print("Ingreso una fecha incorrecta,revise, debería ser YYYY-MM-DD")
                    print()
                    print()   
                    fecha_inicial = input("Ingrese fecha de inicio en formato YYYY-MM-DD:")
                    verificador_fecha_inicial(fecha_inicial) 
                print()
                print()
                fecha_final = input("Ingrese fecha final en formato YYYY-MM-DD:") 
                verificador_fecha_final(fecha_final)
               
                while verificador_fecha_final(fecha_final) == False:
                    print()
                    print()
                    print("Ingreso una fecha incorrecta,revise, debería ser YYYY-MM-DD")
                    print()
                    print()
                    fecha_final = input("Ingrese fecha final en formato YYYY-MM-DD:") 
                    verificador_fecha_final(fecha_final)
 
                logaritmo()
    print()            
    print()
    volver_menu = input("Desea volver al menu principal?(ingrese si/no):")
    if volver_menu == "si":
        print() 
        print()
        menu()
        print() 
        print()
        seleccion = int(input("Por favor seleccione una opción de las 4 posibles:"))  
        limpieza_listas ()
    else:
        print()
        print()
        print("Hasta Luego!")
        print()
        print("By Juan Targize y Melanie Toledo")
        break

if seleccion == 4:
    print()
    print()
    print("Hasta Luego!")
    print()
    print("By Juan Targize y Melanie Toledo")
    

      












                





    