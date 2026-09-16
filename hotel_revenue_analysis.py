# DATOS DEL HOTEL

dias = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo"
]

habitaciones_disponibles = [100, 100, 100, 100, 100, 100, 100]

habitaciones_vendidas = [65, 70, 80, 90, 95, 100, 75]

ingresos_habitaciones = [6500, 7700, 9600, 11700, 13300, 15000, 8250]

print("Los datos del hotel se han cargado correctamente.")

# CALCULAR OCUPACIÓN

ocupacion = []

for i in range(len(dias)):
    porcentaje = (
        habitaciones_vendidas[i]
        / habitaciones_disponibles[i]
    ) * 100

    ocupacion.append(porcentaje)

print("Ocupación:", ocupacion)

# CALCULAR ADR

adr = []

for i in range(len(dias)):
    precio_medio = (
        ingresos_habitaciones[i]
        / habitaciones_vendidas[i]
    )

    adr.append(precio_medio)

print("ADR:", adr)

# CALCULAR REVPAR

revpar = []

for i in range(len(dias)):
    ingreso_por_habitacion = (
        ingresos_habitaciones[i]
        / habitaciones_disponibles[i]
    )

    revpar.append(ingreso_por_habitacion)

print("RevPAR:", revpar)

# INFORME DIARIO

print("\nINFORME DE REVENUE DEL HOTEL")
print("----------------------------")

for i in range(len(dias)):
    print(
        dias[i],
        "| Ocupación:", round(ocupacion[i], 2), "%",
        "| ADR:", round(adr[i], 2), "€",
        "| RevPAR:", round(revpar[i], 2), "€"
    )

# RESUMEN SEMANAL

total_habitaciones_vendidas = sum(habitaciones_vendidas)

total_habitaciones_disponibles = sum(habitaciones_disponibles)

total_ingresos = sum(ingresos_habitaciones)

adr_semanal = (
    total_ingresos
    / total_habitaciones_vendidas
)

ocupacion_semanal = (
    total_habitaciones_vendidas
    / total_habitaciones_disponibles
) * 100

revpar_semanal = (
    total_ingresos
    / total_habitaciones_disponibles
)

print("\nRESUMEN SEMANAL")
print("---------------")

print(
    "Habitaciones vendidas:",
    total_habitaciones_vendidas
)

print(
    "Ingresos totales:",
    total_ingresos,
    "€"
)

print(
    "Ocupación semanal:",
    round(ocupacion_semanal, 2),
    "%"
)

print(
    "ADR semanal:",
    round(adr_semanal, 2),
    "€"
)

print(
    "RevPAR semanal:",
    round(revpar_semanal, 2),
    "€"
)  

# CONCLUSIONES AUTOMÁTICAS

dia_mayor_ocupacion = dias[ocupacion.index(max(ocupacion))]

dia_mayor_adr = dias[adr.index(max(adr))]

dia_mayor_revpar = dias[revpar.index(max(revpar))]

print("\nCONCLUSIONES")
print("------------")

print("Día con mayor ocupación:", dia_mayor_ocupacion)

print("Día con mayor ADR:", dia_mayor_adr)

print("Día con mayor RevPAR:", dia_mayor_revpar)

# GRÁFICO DE OCUPACIÓN

import matplotlib.pyplot as plt

plt.plot(dias, ocupacion, marker="o")

plt.title("Ocupación del hotel por día")
plt.xlabel("Día")
plt.ylabel("Ocupación (%)")

plt.ylim(0, 100)

plt.show()

# GRÁFICO DE ADR

plt.plot(dias, adr, marker="o")

plt.title("ADR del hotel por día")
plt.xlabel("Día")
plt.ylabel("ADR (€)")

plt.show()

# GRÁFICO DE REVPAR

plt.plot(dias, revpar, marker="o")

plt.title("RevPAR del hotel por día")
plt.xlabel("Día")
plt.ylabel("RevPAR (€)")

plt.show()