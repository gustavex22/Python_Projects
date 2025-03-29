
n1 = "2*2"

n2 = n1.find("+")
print(n2)
#devuelve -1 porque  la cadena no esta en la variable

import re

n2 = "(10*1)"
n3 = re.search(r"\((\d+)\)",n2)

print("El numero es: "+n3.group(1))

#? Este codigo toma el numero dentro del entreparentesis ya sea de 1 o 2 digitos

# *Expresiones generales

