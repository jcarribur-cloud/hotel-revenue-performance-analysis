import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hotel Revenue Analysis",
    page_icon="🏨"
)

st.title("🏨 Hotel Revenue Performance Analysis")
# Cargar archivo CSV
archivo_cargado = st.sidebar.file_uploader(
    "Upload hotel CSV file",
    type=["csv"]
)

if archivo_cargado is not None:
    df_csv = pd.read_csv(archivo_cargado)

    st.success("CSV uploaded successfully!")

    st.subheader("Uploaded CSV Preview")

    st.dataframe(
        df_csv,
        use_container_width=True
    )

# Datos del hotel
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

# Datos del hotel

if archivo_cargado is not None:
    columnas_necesarias = [
        "Day",
        "Available Rooms",
        "Sold Rooms",
        "Room Revenue"
    ]

    if all(columna in df_csv.columns for columna in columnas_necesarias):
        dias = df_csv["Day"].astype(str).tolist()

        habitaciones_disponibles = (
            df_csv["Available Rooms"].tolist()
        )

        habitaciones_vendidas = (
            df_csv["Sold Rooms"].tolist()
        )

        ingresos_habitaciones = (
            df_csv["Room Revenue"].tolist()
        )

    else:
        st.error(
            "The CSV must contain: Day, Available Rooms, "
            "Sold Rooms and Room Revenue."
        )

else:
    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    habitaciones_disponibles = [
        100, 100, 100, 100, 100, 100, 100
    ]

    habitaciones_vendidas = [
        65, 70, 80, 90, 95, 100, 75
    ]

    ingresos_habitaciones = [
        6500, 7700, 9600, 11700, 13300, 15000, 8250
    ]

# Cálculos diarios
ocupacion = []
adr = []
revpar = []

for i in range(len(dias)):
    ocupacion_dia = (
        habitaciones_vendidas[i]
        / habitaciones_disponibles[i]
    ) * 100

    adr_dia = (
        ingresos_habitaciones[i]
        / habitaciones_vendidas[i]
    )

    revpar_dia = (
        ingresos_habitaciones[i]
        / habitaciones_disponibles[i]
    )

    ocupacion.append(ocupacion_dia)
    adr.append(adr_dia)
    revpar.append(revpar_dia)

# Resumen semanal
total_habitaciones = sum(habitaciones_disponibles)
total_vendidas = sum(habitaciones_vendidas)
total_ingresos = sum(ingresos_habitaciones)

ocupacion_semanal = (
    total_vendidas / total_habitaciones
) * 100

adr_semanal = total_ingresos / total_vendidas

revpar_semanal = total_ingresos / total_habitaciones

# Indicadores principales
st.subheader("Weekly Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Occupancy",
    f"{ocupacion_semanal:.2f}%"
)

col2.metric(
    "ADR",
    f"€{adr_semanal:.2f}"
)

col3.metric(
    "RevPAR",
    f"€{revpar_semanal:.2f}"
)

col4.metric(
    "Room Revenue",
    f"€{total_ingresos:,.2f}"
)

# Tabla diaria
st.subheader("Daily Performance")

tabla = {
    "Day": dias,
    "Occupancy (%)": [round(x, 2) for x in ocupacion],
    "ADR (€)": [round(x, 2) for x in adr],
    "RevPAR (€)": [round(x, 2) for x in revpar]
}

st.dataframe(tabla, use_container_width=True)

# Convertir la tabla a DataFrame
df = pd.DataFrame(tabla)

# Botón para descargar los resultados
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Daily Performance CSV",
    data=csv,
    file_name="hotel_daily_performance.csv",
    mime="text/csv"
)

# Selector de indicador
st.sidebar.header("Select Metric")

metrica = st.sidebar.selectbox(
    "Choose an indicator:",
    ["Occupancy", "ADR", "RevPAR"]
)

st.write("Selected metric:", metrica)

# Gráfico interactivo
st.subheader("Interactive Performance Chart")

if metrica == "Occupancy":
    st.line_chart({"Occupancy (%)": ocupacion})

elif metrica == "ADR":
    st.line_chart({"ADR (€)": adr})

else:
    st.line_chart({"RevPAR (€)": revpar})

# Conclusiones automáticas
st.subheader("Automatic Conclusions")

dia_mayor_ocupacion = dias[ocupacion.index(max(ocupacion))]
dia_mayor_adr = dias[adr.index(max(adr))]
dia_mayor_revpar = dias[revpar.index(max(revpar))]

st.write(
    f"📈 The highest occupancy was on {dia_mayor_ocupacion} "
    f"with {max(ocupacion):.2f}%."
)

st.write(
    f"💶 The highest ADR was on {dia_mayor_adr} "
    f"with €{max(adr):.2f}."
)

st.write(
    f"🏨 The highest RevPAR was on {dia_mayor_revpar} "
    f"with €{max(revpar):.2f}."
)

# Recomendaciones de Revenue Management
st.subheader("Management Recommendations")

st.write(
    "• Saturday shows the highest demand, so the hotel could consider "
    "increasing room rates."
)

st.write(
    "• Low-demand days could benefit from promotions or special packages."
)

st.write(
    "• Occupancy, ADR and RevPAR should be reviewed together before "
    "making pricing decisions."
)