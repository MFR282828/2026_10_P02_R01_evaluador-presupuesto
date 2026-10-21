# ==============================================================================
# SAGA DE REPOSITORIOS PYTHON 2026
# Repositorio: 2026_10_P02_R01_evaluador-presupuesto
# Principio 2: Control de flujo y estructuras de datos básicas (Nivel: Básico)
# ==============================================================================

# --- ENTRADA DE DATOS ---
print("========================================")
print("        EVALUADOR DE PRESUPUESTO        ")
print("========================================")

actividad = input("Ingrese el nombre de la actividad: ")
presupuesto = float(input("Ingrese el presupuesto disponible (S/): "))
costo_estimado = float(input("Ingrese el costo estimado de la actividad (S/): "))

# --- EVALUACIÓN DE REGLAS DE NEGOCIO Y SALIDA ---
print("\n========================================")
print("         RESUMEN DE EVALUACIÓN          ")
print("========================================")
print("Actividad:", actividad)
print("----------------------------------------")

# Regla 1: Validar presupuesto no positivo
if presupuesto <= 0:
    print("Resultado: Presupuesto no válido")

# Regla 2: Evaluar costo dentro del presupuesto
elif costo_estimado <= presupuesto:
    saldo_restante = presupuesto - costo_estimado
    print("Resultado: Dentro del presupuesto")
    print("Saldo restante: S/", saldo_restante)

# Regla 3: Evaluar exceso presupuestario
else:
    importe_faltante = costo_estimado - presupuesto
    print("Resultado: Exceso presupuestario")
    print("Importe faltante: S/", importe_faltante)

print("========================================")