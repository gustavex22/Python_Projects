"""[Nuevo Projecto]
 #* Calculadora de ecuaciones
    1. como funcionaria?
    Meter una Ecuacion cualquiera y que devuelva la posible solucion a esta
    
    2.Pasos
    1.0Jerarquia de ecuaciones
    1.1. Ecuaciones lineales [Primer test]
    1.2 Ecuaciones cuadraticas [Segundo test]
    
    
    resumen:
  #*  El projecto de calculadora de ecuaciones debe de hacer estas cosas
    
    1. permitir meter ecuaciones lineales y cuadraticas
     1.1dividir la ecuacion por jerarquias
     1.2. resolver las divisiones
     
     1.3 Adaptar la formula fórmula de Bhaskar para las ecuaciones cuadraticas
    2.Respetar la jerarquia de ecuaciones
    3.Adaptar los metodos de resolucion de las Ecuaciones a codigo
    
    !!Restriccion = NO USAR EVAL()

"""
import math

def resolucion_ecuaciones(ecuacion):
  Operacion = ecuacion.split("=")
  P1 = Operacion [0]
  P2 = Operacion [1]

  index_inicio = P1.find("(")+1 #1
  index_fin = P1.find(")") #4
  P1 = P1[index_inicio :index_fin]
    
  if P1.find("*") != -1 :
    operation = "*"
  elif P1.find("/") != -1:
    operation = "/"
  elif P1.find("+") != -1:
    operation = "+"
  elif P1.find("-") != -1:
    operation = "-"
    
  P1 = P1.split(operation)

  n1 = int(P1[0])
  n2 =int(P1[1])

  if operation == "*":
    P1 = n1 * n2
  elif operation == "/":
    P1 = n1 / n2
  elif operation == "+":
    P1 = n1 + n2
  elif operation == "-":
    P1 = n1 - n2


  return P1

  
  
  
        
        
print("Calculadora de Ecuaciones")
#Ecuacion =str( input("Introduzca una Ecuacion Lineal"))
Ecuacion = "(2*4)=16"  #resultado 
print(Ecuacion)
number_limpio = resolucion_ecuaciones(Ecuacion)

Ecuacion = Ecuacion.split("=")
Ecuacion = int(Ecuacion[1])

print(f"{number_limpio} = {Ecuacion}")

resultado =int( Ecuacion / number_limpio)

print(resultado)








# *  String de ejemplo  = 2* 2 +2

#? jerarquia de ecuaciones

"""1. ()
      2. ()2
      3. *  and  /
      4. +  and -
      
      en las 2 ultimas se resuelven de izquierda a derecha
"""







