# Evaluador de Presupuesto

Programa de consola (CLI) desarrollado en Python para evaluar si el costo estimado de una actividad se ajusta al presupuesto disponible, identificando excedentes o presupuestos no válidos mediante condicionales.

## Objetivo

Demostrar el uso de estructuras de control de flujo condicionales (`if`, `elif`, `else`) y operadores de comparación (`<=`) para evaluar reglas de negocio secuenciales sobre montos presupuestarios.

---

## Entradas

El programa solicita tres datos por consola:
1. **Nombre de la actividad:** Texto descriptivo de la actividad.
2. **Presupuesto disponible:** Monto numérico convertido a `float`.
3. **Costo estimado:** Monto numérico convertido a `float`.

---

## Reglas de negocio y fórmulas

1. **Presupuesto no válido:**
   - **Condición:** Presupuesto disponible es menor o igual a cero (`presupuesto <= 0`).
   - **Mensaje:** `Presupuesto no válido`.

2. **Dentro del presupuesto:**
   - **Condición:** Presupuesto mayor a cero y costo estimado menor o igual al presupuesto (`costo_estimado <= presupuesto`).
   - **Fórmula:** `saldo_restante = presupuesto_disponible - costo_estimado`
   - **Mensaje:** `Dentro del presupuesto` junto con el saldo restante.

3. **Exceso presupuestario:**
   - **Condición:** Presupuesto mayor a cero y costo estimado mayor al presupuesto (`costo_estimado > presupuesto`).
   - **Fórmula:** `importe_faltante = costo_estimado - presupuesto_disponible`
   - **Mensaje:** `Exceso presupuestario` junto con el importe faltante.

---

## Casos de prueba obligatorios

| Presupuesto | Costo estimado | Resultado esperado | Detalle calculado |
| :---: | :---: | :--- | :--- |
| `1,000` | `750` | Dentro del presupuesto | Saldo restante: `250.0` |
| `1,000` | `1,000` | Dentro del presupuesto | Saldo restante: `0.0` |
| `1,000` | `1,200` | Exceso presupuestario | Importe faltante: `200.0` |
| `0` | `200` | Presupuesto no válido | Sin cálculos adicionales |
| `1,000` | `0` | Dentro del presupuesto | Saldo restante: `1,000.0` |

---

## Principio trabajado

- **Principio Principal:** **Principio 2. Control de flujo y estructuras de datos básicas** (Nivel: Básico)

### Mapa de Principios de la Saga Python 2026

- [X] **Principio 1. Fundamentos del lenguaje Python**
- [X] **Principio 2. Control de flujo y estructuras de datos básicas**
- [ ] Principio 3. Funciones, parámetros y alcance de variables
- [ ] Principio 4. Manejo de errores y excepciones
- [ ] Principio 5. Comprensiones y código idiomático de Python
- [ ] Principio 6. Calidad del código y convenciones profesionales
- [ ] Principio 7. Programación Orientada a Objetos (POO)
- [ ] Principio 8. Complejidad algorítmica y análisis de eficiencia
- [ ] Principio 9. Módulos, paquetes y reutilización de código
- [ ] Principio 10. PIP, entornos virtuales y dependencias
- [ ] Principio 11. Aplicaciones CRUD y persistencia de datos
- [ ] Principio 12. Testing y validación automatizada
- [ ] Principio 13. Estadística computacional, simulación y programación dinámica
- [ ] Principio 14. Arquitectura de proyectos y distribución de paquetes
- [ ] Principio 15. Principios SOLID y patrones de diseño

---

## Instrucciones de configuración y ejecución

### 1. Crear y activar el entorno virtual (`venv`)

En Windows (PowerShell):
```powershell
python -m venv --copies .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1