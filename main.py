from datetime import datetime

from funciones import (
    calcular_base_imponible,
    calcular_descuentos,
    calcular_promedios,
    ingresar_dato,
)


def main():
    empleados = []

    print("Registro de datos para 10 empleados:")
    for i in range(10):
        print(f"\nEmpleado {i + 1}:")
        nombre = ingresar_dato("Ingrese el nombre: ", str)
        apellido = ingresar_dato("Ingrese el apellido: ", str)
        sueldo_base = ingresar_dato(
            "Ingrese el sueldo base (número positivo): ", float, lambda x: x > 0
        )
        fecha_ingreso = ingresar_dato("Ingrese la fecha de ingreso (YYYY-MM-DD): ", str)
        cantidad_hijos = ingresar_dato(
            "Ingrese la cantidad de hijos (entero >= 0): ", int, lambda x: x >= 0
        )
        empresa_sso = ingresar_dato(
            "Ingrese la empresa SSO (1 o 2): ", int, lambda x: x in [1, 2]
        )

        try:
            fecha_ingreso_dt = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
            meses_trabajados = (
                (datetime.now().year - fecha_ingreso_dt.year) * 12
                + datetime.now().month
                - fecha_ingreso_dt.month
            )
            if meses_trabajados < 0:
                raise ValueError("La fecha de ingreso no puede ser futura.")
        except ValueError:
            print("Error: Fecha de ingreso inválida. Se asignarán 0 meses trabajados.")
            meses_trabajados = 0

        base_imponible = calcular_base_imponible(
            sueldo_base, meses_trabajados, cantidad_hijos
        )
        salud, sso = calcular_descuentos(base_imponible, empresa_sso)

        empleados.append(
            {
                "nombre": nombre,
                "apellido": apellido,
                "sueldo_base": sueldo_base,
                "base_imponible": base_imponible,
                "salud": salud,
                "sso": sso,
                "empresa_sso": empresa_sso,
            }
        )

    promedio_salud, promedio_sso = calcular_promedios(empleados)

    print("\nResumen de datos de empleados:")
    for empleado in empleados:
        print(
            f"{empleado['nombre']} {empleado['apellido']} - Base imponible: {empleado['base_imponible']:.2f}, Salud: {empleado['salud']:.2f}, SSO: {empleado['sso']:.2f}"
        )

    print(f"\nPromedio de pago en salud: {promedio_salud:.2f}")
    print(f"Promedio de pago en SSO: {promedio_sso:.2f}")


if __name__ == "__main__":
    main()
