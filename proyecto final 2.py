# Convertidor de unidades, empleando conversiones de masa y longitud
# Primero, se crean dos diccionarios que en este caso son "masa" y "longitud", estos mismos contienen unidades de medida y sus equivalencias en kilogramos y metros
masa = {
    "tonelada": 1000,        # 1 tonelada = 1000[kg]
    "kilogramo": 1,          # esta es su unidad base
    "gramo": 0.001,          # 1 gramo = 0.001[kg]
    "miligramo": 1e-6        # 1 miligramo = 0.000001[kg]
}
longitud = {
    "pulgada": 0.0254,       # 1 pulgada = 0.0254[m]
    "pie": 0.3048,           # 1 pie = 0.3048[m]
    "yarda": 0.9144,         # 1 yarda = 0.9144[m]
    "metro": 1               # unidad base
}
# se muestra un mensaje que le advierte al usuario la importancia de utilizar unidades del mismo tipo
print("\033[1m" "antes de proceder con la conversion debe asegurarse de que las unidades de conversion que se ingresen deben ser del mismo tipo" "\033[0m")
inicio = input("\033[1m" "Ingresar la unidad a converir \033[0m (tonelada, kilogramo, gramo, miligramo, pulgada, pie, yarda, metro): ")
fin = input("\033[1m" "Ingresar el tipo de unidad en la que se imprima la conversion \033[0m (tonelada, kilogramo, gramo, miligramo, pulgada, pie, yarda, metro): ")
dato = float(input("Ingrese el dato a convertir: "))
# este bloque quiere decir que el programa realizara esta operacion si tanto la unidad de inicio como la de fin están en el grupo "masa"
if inicio in masa and fin in masa:
    kg = dato * masa[inicio]       
    conversion = kg / masa[fin] 
    print(f"conversion: {dato} {inicio} es igual a {conversion} {fin}")
# si no se cumple el primer if, se pasa a este "elif", que se ejecuta si inicio y fin están en el grupo "longitud"
elif inicio in longitud and fin in longitud:
    metros = dato * longitud[inicio]      
    conversion = metros / longitud[fin] 
    print(f"conversion: {dato} {inicio} es igual a {conversion} {fin}")
else:
    print("\033[1m" "Esa conversion no esta asignada" "\033[0m")
