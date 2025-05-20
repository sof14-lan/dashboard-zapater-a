import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard de Inteligencia Comercial", layout="wide")

st.title("📊 Dashboard Interactivo - Análisis Regional")

# Datos
datos_ingreso = pd.DataFrame({
    'País': ['Costa Rica', 'Nicaragua', 'Honduras', 'El Salvador', 'Guatemala', 'Panamá'],
    'Regulaciones Aduaneras': [4, 1, 3, 3, 3, 2],
    'Competencia Local': [2, 2, 4, 3, 2, 3],
    'Costos de Transporte': [1, 1, 3, 3, 2, 3],
    'Aranceles': [4, 4, 4, 4, 2, 3]
})

datos_demanda = pd.DataFrame({
    'País': ['Costa Rica', 'Nicaragua', 'Honduras', 'El Salvador', 'Guatemala', 'Panamá'],
    'Demanda Hombre': [30312, 31631, 27591, 38837, 38655, 43771],
    'Demanda Mujer': [24002, 34877, 54269, 50484, 18998, 23428]
})

datos_riesgo = pd.DataFrame({
    'País': ['Costa Rica', 'Nicaragua', 'Honduras', 'El Salvador', 'Guatemala', 'Panamá'],
    'Riesgo Político': [8, 1, 2, 8, 8, 8],
    'Riesgo Económico': [6, 7, 3, 2, 6, 2],
    'Riesgo Social': [5, 5, 3, 3, 7, 9]
})

datos_competencia = pd.DataFrame({
    'País': ['Costa Rica', 'Nicaragua', 'Honduras', 'El Salvador', 'Guatemala', 'Panamá'],
    'Competidor A': [28835, 7002, 18228, 12837, 28364, 11578],
    'Competidor B': [13061, 6311, 24347, 23772, 23990, 24784],
    'Competidor C': [14843, 17046, 19676, 6860, 19433, 3413]
})

# Sidebar
st.sidebar.title("🔍 Filtro")
pais_seleccionado = st.sidebar.selectbox("Selecciona un país", datos_ingreso['País'].unique())

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🌍 Factores de Ingreso", "📈 Demanda", "⚠️ Riesgos", "🏢 Competencia"])

with tab1:
    st.subheader("Factores de Ingreso al Mercado")
    datos = datos_ingreso[datos_ingreso['País'] == pais_seleccionado].drop(columns=["País"])
    st.bar_chart(datos.T)

with tab2:
    st.subheader("Demanda por Género")
    datos = datos_demanda[datos_demanda['País'] == pais_seleccionado].drop(columns=["País"])
    fig = px.pie(
        names=datos.columns.tolist(),
        values=datos.values.flatten().tolist(),
        title=f"Distribución de la Demanda en {pais_seleccionado}",
        hole=0.4
    )
    st.plotly_chart(fig)

with tab3:
    st.subheader("Riesgos del País")
    datos = datos_riesgo[datos_riesgo['País'] == pais_seleccionado].drop(columns=["País"])
    fig = px.bar(
        x=datos.columns.tolist(),
        y=datos.values.flatten().tolist(),
        labels={"x": "Tipo de Riesgo", "y": "Nivel"},
        title=f"Niveles de Riesgo en {pais_seleccionado}",
        color=datos.values.flatten().tolist(),
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig)

with tab4:
    st.subheader("Análisis de la Competencia")
    datos = datos_competencia[datos_competencia['País'] == pais_seleccionado].drop(columns=["País"])
    fig = px.bar(
        x=datos.columns.tolist(),
        y=datos.values.flatten().tolist(),
        labels={"x": "Competidor", "y": "Presencia de Mercado"},
        title=f"Competencia en {pais_seleccionado}",
        color=datos.values.flatten().tolist(),
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig)

st.markdown("---")
st.caption("Desarrollado con 💡 por Tannia Hernández Martínez")

