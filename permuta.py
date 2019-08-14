#!/bin/python3
# este programa sirve para calcular las combinaciones o permutaciones 
import math
import sys
import re

numeros = 10
minusculas = 26
mayusculas  = 26
caracteresImprime = 32


## -------              FUNCIONES DE PERMUTACION

def permutacion_con_repeticion(cant_caracteres,largo):
        return math.pow(cant_caracteres,int(largo) ) 

def permutacion_sin_repeticion(cant_caracteres,largo):
        return (math.factorial(cant_caracteres) / math.factorial(cant_caracteres - int(largo) ) )



def cantidad_caracteres(caracteres):                    # esta funcion chequea las opciones de nmM (numeros, minusculas y mayusculas ), 
                                                                                                # imprime las opciones utilizadas y devuelve el valor de la suma de caracteres.
        global numeros
        global minusculas
        global mayusculas
        global caracteresImprime

        utiliza = ""
        n = 0 

        if re.findall("n",caracteres):          # busca la letra n 

                utiliza+=" - Numeros"
                n += numeros

        if re.findall("m", caracteres):         # busca la letra m

                utiliza +=" - Minusculas"
                n += minusculas

        if re.findall("M", caracteres):         # busca la letra M
                utiliza +=" - Mayusculas"
                n += mayusculas

        if re.findall("C", caracteres):
                utiliza +=" - Caracteres Imprimibles"
                n += caracteresImprime

        if re.search("\d", caracteres):
                utiliza += " Personalizados "
                n = int (caracteres)

        print ("Caracteres utilizados                      [ "+ utiliza +" ]")
        return n                                                        # devuelve la suma de los caracteres

def ayuda():
        print ('''
    ____  __________  __  _____  ___________   ______________  _   _____________
   / __ \/ ____/ __ \/  |/  / / / /_  __/   | / ____/  _/ __ \/ | / / ____/ ___/
  / /_/ / __/ / /_/ / /|_/ / / / / / / / /| |/ /    / // / / /  |/ / __/  \__ \
 / ____/ /___/ _, _/ /  / / /_/ / / / / ___ / /____/ // /_/ / /|  / /___ ___/ /
/_/   /_____/_/ |_/_/  /_/\____/ /_/ /_/  |_\____/___/\____/_/ |_/_____//____/
                                                         v1.0   by phr4nt0m


MODO DE USO:

python3 permuta.py [TIPO DE PERMUTACION] [CARACTERES] [LARGO DE CADENA]

        [ TIPO DE PERMUTACION ]

                -c Con repeticion.
                -s Sin repeticion.

        [ CARACTERES A UTILIZAR ]

                n       Numero decimales (0-9).
                m       Letras minusculas.
                M       Letras Mayusculas.
                C       Caracteres imprimibles !@#$%^&*();:;/?,.<>[]{}

        [ CARACTERES PERSONALIZADO ]

                [0..99999] Numero entero de caracteres a permutar.

        -h Ayuda

Ejemplos de uso:
        python3 permuta.py -c nmM 8

        python3 permuta.py -c 10 5

        ''')


##### -------------------------------------------------------------------------------
try:

        cant_caracteres = cantidad_caracteres(sys.argv[2])
        print("Total de caracteres a utilizar :           [ %d ]" %(cant_caracteres)) 


        if sys.argv[1]=="-c":

                print ("Total permutaciones con repeticion :       [ %d ] " %(permutacion_con_repeticion(cant_caracteres, sys.argv[3])) )


        elif sys.argv[1]=="-s":

                print ("Total permutaciones sin repeticion :       [ %d ]" %(permutacion_sin_repeticion(cant_caracteres, sys.argv[3])) )


        elif sys.argv[1]=="-h":

                ayuda()

        else:

                print("Opcion no valida!")

except:

        ayuda()




