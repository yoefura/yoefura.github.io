import streamlit as st
import pandas as pd

# Configuración del entorno web
st.set_page_config(
    page_title="Tabla de Verdad - Caso 3", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo visual adaptado a la temática ambiental de la imagen
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1f1d;
        background-image: linear-gradient(135deg, #071412 0%, #0d2822 100%);
        color: #e0f2f1;
    }
    h1 {
        color: #4caf50 !important;
        font-family: 'Arial Black', Gadget, sans-serif;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    h3 {
        color: #81c784 !important;
        font-weight: bold;
        border-bottom: 2px solid #2e7d32;
        padding-bottom: 5px;
    }
    .panel-header {
        background-color: #112d24;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #2e7d32;
        margin-bottom: 20px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="panel-header"><h1>TABLA DE VERDAD</h1><p style="color:#81c784; font-weight:bold; margin:0;">CASO 3: CONTROL DE CONTAMINACIÓN AMBIENTAL</p></div>', unsafe_allow_html=True)

# Sección de Variables
st.subheader("📌 VARIABLES DEL MODELO")
col_v1, col_v2, col_v3 = st.columns(3)
with col_v1:
    st.markdown("**p:** Se reducen las emisiones contaminantes.")
with col_v2:
    st.markdown("**q:** Se implementan políticas ambientales.")
with col_v3:
    st.markdown("**r:** Mejora la calidad del aire.")

# Nueva Fórmula Lógica
st.subheader("📐 FÓRMULA LÓGICA DEL CASO")
st.info("Evaluación conjunta de las condiciones de impacto:")
st.latex(r"(p \rightarrow r) \land (q \rightarrow r)")

# Panel Interactivos (Estado de los interruptores)
st.subheader("🎛️ ESTADO ACTUAL DE LOS ENUNCIADOS")
col1, col2, col3 = st.columns(3)
with col1:
    val_p = st.checkbox("Se reducen emisiones (p)", value=False)
with col2:
    val_q = st.checkbox("Se implementan políticas (q)", value=False)
with col3:
    val_r = st.checkbox("Mejora la calidad del aire (r)", value=False)

# Operaciones lógicas basadas estrictamente en la nueva tabla
cond_p_r = not val_p or val_r
cond_q_r = not val_q or val_r
resultado_final = cond_p_r and cond_q_r

# Mensaje del Sistema e Interpretación
st.subheader("📢 INTERPRETACIÓN DEL ESCENARIO")
if resultado_final:
    st.success(
        "🟢 **Fórmula VERDADERA:** Lógicamente válido y consistente con el diseño del control ambiental."
    )
else:
    st.error(
        "🔴 **Fórmula FALSA:** El resultado (r) NO se cumple, pero al menos una de las acciones (p o q) sí se ejecutó. Esto invalida el modelo."
    )

# Nueva Tabla de Verdad idéntica a la imagen
st.subheader("📊 MATRIZ DE EVALUACIÓN COMPLETA")

filas = []
# Mismo orden de filas que tu imagen (V,V,V -> V,V,F -> V,F,V ...)
for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            p_r = not p or r
            q_r = not q or r
            final = p_r and q_r
            filas.append({
                "p (Emisiones)": "V" if p else "F",
                "q (Políticas)": "V" if q else "F",
                "r (Calidad Aire)": "V" if r else "F",
                "p → r": "V" if p_r else "F",
                "q → r": "V" if q_r else "F",
                "Resultado Final (Fórmula)": "🟢 V" if final else "🔴 F"
            })

df_tabla = pd.DataFrame(filas)

# Función para resaltar la fila activa según las casillas marcadas
def resaltar_fila_activa(row):
    match_p = row["p (Emisiones)"] == ("V" if val_p else "F")
    match_q = row["q (Políticas)"] == ("V" if val_q else "F")
    match_r = row["r (Calidad Aire)"] == ("V" if val_r else "F")
    
    if match_p and match_q and match_r:
        return ['background-color: #1b4d3e; color: #fff; font-weight: bold'] * len(row)
    return [''] * len(row)

st.dataframe(df_tabla.style.apply(resaltar_fila_activa, axis=1), use_container_width=True)
