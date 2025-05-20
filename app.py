import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Análisis Regional", layout="wide")

st.title("📊 Dashboard Interactivo: Evaluación de Países Centroamericanos")

# Datos
rank_data = {
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Regulaciones Aduaneras": [4, 1, 3, 3, 3, 2],
    "Competencia Local": [2, 2, 4, 3, 2, 3],
    "Costos de Transporte": [1, 1, 3, 3, 2, 3],
    "Aranceles": [4, 4, 4, 4, 2, 3]
}

demanda_data = {
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Demanda Hombre": [30312, 31631, 27591, 38837, 38655, 43771],
    "Demanda Mujer": [24002, 34877, 54269, 50484, 18998, 23428]
}

riesgo_data = {
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Riesgo Político": [8, 1, 2, 8, 8, 8],
    "Riesgo Económico": [6, 7, 3, 2, 6, 2],
    "Riesgo Social": [5, 5, 3, 3, 7, 9]
}

competidores_data = {
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Competidor A": [28835, 7002, 18228, 12837, 28364, 11578],
    "Competidor B": [13061, 6311, 24347, 23772, 23990, 24784],
    "Competidor C": [14843, 17046, 19676, 6860, 19433, 3413]
}

# Convertir a DataFrames
df_rank = pd.DataFrame(rank_data)
df_demanda = pd.DataFrame(demanda_data)
df_riesgo = pd.DataFrame(riesgo_data)
df_competidores = pd.DataFrame(competidores_data)

# Filtro de país
pais_seleccionado = st.selectbox("Seleccioná un país para analizar:", df_rank["País"])

# Layout de columnas
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Indicadores de Mercado")
    st.dataframe(df_rank[df_rank["País"] == pais_seleccionado].set_index("País"))

    fig_rank = px.bar(
        df_rank[df_rank["País"] == pais_seleccionado].melt(id_vars=["País"]),
        x="variable", y="value", color="variable",
        title="Ranking de Regulaciones, Competencia, Transporte y Aranceles",
        labels={"variable": "Categoría", "value": "Nivel"}
    )
    st.plotly_chart(fig_rank)

with col2:
    st.subheader("📈 Demanda por Género")
    fig_demanda = px.bar(
        df_demanda[df_demanda["País"] == pais_seleccionado].melt(id_vars=["País"]),
        x="variable", y="value", color="variable",
        title="Demanda Masculina y Femenina",
        labels={"variable": "Género", "value": "Cantidad"}
    )
    st.plotly_chart(fig_demanda)

st.subheader("⚠️ Riesgos País (Político, Económico y Social)")
fig_riesgo = px.bar(
    df_riesgo[df_riesgo["País"] == pais_seleccionado].melt(id_vars=["País"]),
    x="variable", y="value", color="variable",
    title="Riesgo País",
    labels={"variable": "Tipo de Riesgo", "value": "Nivel"}
)
st.plotly_chart(fig_riesgo)

st.subheader("📊 Presencia de Competidores")
fig_comp = px.bar(
    df_competidores[df_competidores["País"] == pais_seleccionado].melt(id_vars=["País"]),
    x="variable", y="value", color="variable",
    title="Competidores por País",
    labels={"variable": "Competidor", "value": "Cantidad de Productos"}
)
st.plotly_chart(fig_comp)
