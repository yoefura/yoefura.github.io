import streamlit as st
import pandas as pd

# Configuración del entorno web
st.set_page_config(
    page_title="Modelo de Calidad del Aire", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo visual con temática del medio ambiente
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f7f5;
        background-image: linear-gradient(135deg, rgba(220,237,225,0.6) 0%, rgba(244,247,245,1) 100%);
    }
    h1 {
        color: #1b4332 !important;
        font-family: Arial, sans-serif;
        font-weight: bold;
    }
    h3 {
        color: #2d6a4f !important;
        font-weight: bold;
        border-bottom: 2px solid #b7e4c7;
        padding-bottom: 5px;
    }
    .card-ambiental {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-left: 5px solid #40916c;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌱 Análisis Lógico de Contaminación Ambiental")
st.write("Herramienta interactiva para evaluar el impacto de las acciones ambientales en el aire.")

# Definición clara de las variables
st.markdown("""
<div class="card-ambiental">
    <h3>📋 Enunciados del Modelo</h3>
    <ul>
        <li><b>p:</b> Se reducen las emisiones contaminantes.</li>
        <li><b>q:</b> Se aplican políticas ambientales.</li>
        <li><b>r:</b> Mejora la calidad del aire.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.subheader("📐 Regla Lógica")
st.write("Si se reducen las emisiones (p) Y se aplican políticas (q), entonces debe mejorar la calidad del aire (r):")
st.latex(r"(p \land q) \rightarrow r")

# Botones de control con nombres naturales
st.subheader("🎛️ Estado Actual de los Enunciados")
st.write("Activa o desactiva las condiciones para ver cómo responde el modelo:")

col1, col2, col3 = st.columns(3)
with col1:
    val_p = st.checkbox("Se reducen emisiones (p)", value=False)
with col2:
    val_q = st.checkbox("Se aplican políticas (q)", value=False)
with col3:
    val_r = st.checkbox("Mejora el aire (r)", value=False)

# Evaluación de la regla condicional
antecedente = val_p and val_q
regla_se_cumple = not antecedente or val_r

# Mensajes directos y naturales
st.subheader("📢 Mensaje del Sistema")

if regla_se_cumple:
    st.success(
        "✅ **¡Es así!** Los enunciados seleccionados cumplen con la regla establecida."
    )
else:
    st.error(
        "❌ **¡No es así!** Se redujeron las emisiones y se aplicaron políticas, pero el aire NO mejoró. "
        "Esto contradice directamente la regla del modelo."
    )

# Tabla de Verdad
st.subheader("📊 Tabla de Verdad del Modelo")

filas = []
for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            ant = p and q
            regla = not ant or r
            filas.append({
                "p (Emisiones)": "Verdadero" if p else "Falso",
                "q (Políticas)": "Verdadero" if q else "Falso",
                "r (Calidad Aire)": "Verdadero" if r else "Falso",
                "Operación (p ∧ q)": "Verdadero" if ant else "Falso",
                "Resultado de la Regla": "V" if regla else "F"
            })

df_tabla = pd.DataFrame(filas)

# Función de resaltado corregida (en singular)
def resaltar_escenario_activo(row):
    match_p = row["p (Emisiones)"] == ("Verdadero" if val_p else "Falso")
    match_q = row["q (Políticas)"] == ("Verdadero" if val_q else "Falso")
    match_r = row["r (Calidad Aire)"] == ("Verdadero" if val_r else "Falso")
    
    if match_p and match_q and match_r:
        return ['background-color: #d8f3dc; color: #1b4332; font-weight: bold'] * len(row)
    return [''] * len(row)

# Mostrar la tabla en la web
st.dataframe(df_tabla.style.apply(resaltar_escenario_activo, axis=1), use_container_width=True)
