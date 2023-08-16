# Definir los sueldos de Juan en cada mes
sueldos = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]

# Calcular el sueldo promedio
sueldo_promedio = sum(sueldos) / len(sueldos)

# Determinar la categoría de sueldo
categoria = ""
if sueldo_promedio < 300:
    categoria = "Sueldo bajo"
elif sueldo_promedio >= 300 and sueldo_promedio <= 900:
    categoria = "Sueldo normal"
else:
    categoria = "Sueldo mejor de lo normal"

# Mostrar los resultados
print(f"El sueldo promedio de Juan es: {sueldo_promedio} dólares")
print(f"Categoría de sueldo: {categoria}")
