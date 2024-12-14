# Función para validar entrada
def ingresar_dato(prompt, tipo_dato, validacion=None):
    while True:
        try:
            dato = tipo_dato(input(prompt))
            if validacion and not validacion(dato):
                raise ValueError("Dato fuera de los parámetros permitidos.")
            return dato
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente nuevamente.")


# Función para calcular la base imponible
def calcular_base_imponible(sueldo_base, meses_trabajados, hijos):
    bonificacion = 0.01 * sueldo_base * meses_trabajados
    asignacion_familiar = 0.05 * sueldo_base * hijos
    return sueldo_base + bonificacion + asignacion_familiar


# Función para calcular descuentos de salud y SSO
def calcular_descuentos(base_imponible, empresa_sso):
    salud = 0.07 * base_imponible
    sso = base_imponible * (0.12 if empresa_sso == 1 else 0.114)
    return salud, sso


# Función para calcular promedios
def calcular_promedios(datos_empleados):
    total_salud = sum(empleado["salud"] for empleado in datos_empleados)
    total_sso = sum(empleado["sso"] for empleado in datos_empleados)
    promedio_salud = total_salud / len(datos_empleados)
    promedio_sso = total_sso / len(datos_empleados)
    return promedio_salud, promedio_sso
