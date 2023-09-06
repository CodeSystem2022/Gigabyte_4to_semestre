import math
from decimal import Decimal
# manejo de valores infinitos

infinito_positivo = float('inf')
print(f'Infinito positivo: {infinito_positivo}')
print(f"es infinito: {math.isinf(infinito_positivo)}") #Pregunta si es infinito

infinito_negativo = float('-inf')
print(f'Infinito negativo: {infinito_negativo}')
print(f"es infinito: {math.isinf(infinito_negativo)}") #Pregunta si es infinito



#Modulo math

infinito_positivo = math.inf
print(f'Infinito positivo: {infinito_positivo}')
print(f"es infinito: {math.isinf(infinito_positivo)}") #Pregunta si es infinito

infinito_negativo = -math.inf
print(f'Infinito negativo: {infinito_negativo}')
print(f"es infinito: {math.isinf(infinito_negativo)}") #Pregunta si es infinito


#Modulo decimal
infinito_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinito_positivo}')
print(f"es infinito: {math.isinf(infinito_positivo)}") #Pregunta si es infinito

infinito_negativo = Decimal('-Infinity')
print(f'Infinito negativo: {infinito_negativo}')
print(f"es infinito: {math.isinf(infinito_negativo)}") #Pregunta si es infinito

