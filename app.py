import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Comercial", layout="wide")

st.title("🌍 Dashboard de Evaluación Comercial por País")

# -----------------------------
# Datos
# -----------------------------

# Ranking
rank_data = {
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Regulaciones Aduaneras": [4, 1, 3, 3, 3, 2],
    "Competencia Local": [2, 2, 4, 3, 2, 3],
    "Costos de Transporte": [1, 1, 3, 3, 2, 3],
    "Aranceles": [4, 4, 4, 4, 2, 3]
}
df_rank = pd.DataFrame(rank_data)

# Demanda
demanda_data = {
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Demanda Hombre": [30312, 31631, 27591, 38837, 38655, 43771],
    "Demanda Mujer": [24002, 34877, 54269, 50484, 18998, 23428]
}
df_demanda = pd.DataFrame(demanda_data)

# Riesgos
riesgo_data = {
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Riesgo Político": [8, 1, 2, 8, 8, 8],
    "Riesgo Económico": [6, 7, 3, 2, 6, 2],
    "Riesgo Social": [5, 5, 3, 3, 7, 9]
}
df_riesgo = pd.DataFrame(riesgo_data)

# Competidores
competencia_data = {
    "País": ["Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Panamá"],
    "Competidor A": [28835, 7002, 18228, 12837, 28364, 11578],
    "Competidor B": [13061, 6311, 24347, 23772, 23990, 24784],
    "Competidor C": [14843, 17046, 19676, 6860, 19433, 3413]
}
df_competencia = pd.DataFrame(competencia_data)

# -----------------------------
# Interfaz
# -----------------------------
pais = st.selectbox("Selecciona un país para ver su análisis:", df_rank["País"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Ranking Logístico y Comercial")
    st.dataframe(df_rank[df_rank["País"] == pais].set_index("País"))

    st.subheader("📈 Demanda por Género")
    st.dataframe(df_demanda[df_demanda["País"] == pais].set_index("País"))

with col2:
    st.subheader("⚠️ Riesgos del Entorno")
    st.dataframe(df_riesgo[df_riesgo["País"] == pais].set_index("País"))

    st.subheader("🤝 Competidores por País")
    st.dataframe(df_competencia[df_competencia["País"] == pais].set_index("País"))

st.markdown("---")
st.caption("Desarrollado por Tannia Hernández Martínez – Comercio y Negocios Internacionales")
