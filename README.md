```
    ____  __________  __  _____  ___________   ______________  _   _____________	
   / __ \/ ____/ __ \/  |/  / / / /_  __/   | / ____/  _/ __ \/ | / / ____/ ___/	
  / /_/ / __/ / /_/ / /|_/ / / / / / / / /| |/ /    / // / / /  |/ / __/  \__ \		
 / ____/ /___/ _, _/ /  / / /_/ / / / / ___ / /____/ // /_/ / /|  / /___ ___/ /		
/_/   /_____/_/ |_/_/  /_/\____/ /_/ /_/  |_\____/___/\____/_/ |_/_____//____/		
                                                         v1.0   by phr4nt0m		
```

# Permutaciones 


## PERMUTACIONES Y COMBINACIONES:
------------------------------

Generalmente se utilizan las palabras combinacion y permutacion como sinonimos, algo totalmente equivocado, asi que para 
que queden claros algunos conceptos paso a dejar algunas definiciones:

Combinacion es la mezcla de los elementos de un conjunto sin importar el orden.
	
ejemplo:
	
	Mi ensalada es una combinacion de tomates, lechugas y cebollas, no importa el 
	orden en que la preparamos si fue tomate, lechuga y cebolla o si fue cebolla, 
	lechuga y tomate, es lo mismo.


Permutación es la variación del orden o posición de los elementos de un conjunto ordenado, donde si importa el orden.

Ejemplo:
	Candado con cerradura de permutacion, en estos candados no es lo mismo 123 que 321 o 213.

Dentro de las permutaciones hay de 2 tipos, con repeticion de elementos y sin repeticion. 

		
## PROGRAMA:
--------
Este programa nos dara la cantidad que permutaciones disponibles para cierta cantidad de elementos y la longitud del mismo 





### REQUISITOS:
----------
 
``` python3:	apt-get install python3 ```




### MODO DE USO:
-----------
```
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
```



### EJEMPLOS DE USO:
---------------

Si queremos ver la cantidad de permutaciones con numeros, letras minusculas y mayusculas en una longitud de 8 caracteres:

`python3 permuta.py -c nmM 8`



Si queremos ver la cantidad de permutaciones entre 10 elementos y con una longitud de 5, usaremos el siguiente comando: 

        `python3 permuta.py -c 10 5`


