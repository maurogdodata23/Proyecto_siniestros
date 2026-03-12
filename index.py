import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns   
import streamlit as st

ruta = "https://github.com/maurogdodata23/Proyecto_siniestros/raw/refs/heads/main/Siniestros_nacionales_aleatorio_trim6.csv"
df = pd.read_csv(ruta, encoding='latin-1', on_bad_lines="skip", sep=';')


# CONFIGURACIÓN BÁSICA

st.set_page_config(page_title="Análisis de Siniestros", page_icon=":⚠️:", layout="wide")

st.title("⚠️ Analisis de Siniestros Nacionales")
st.write("""En el contexto de la seguridad vial y la prevención de accidentes, el análisis de siniestros nacionales representa una herramienta fundamental para comprender las dinámicas que afectan a la sociedad. Este estudio se basa en un conjunto de datos aleatorios que abarca diversos aspectos de los incidentes viales, incluyendo causas, ubicaciones geográficas, condiciones climáticas y perfiles de los involucrados. A través de técnicas de análisis de datos y visualizaciones interactivas, se busca identificar patrones recurrentes, tendencias temporales y factores de riesgo que contribuyan a la ocurrencia de estos eventos. El objetivo principal es proporcionar insights accionables que permitan a las autoridades y la comunidad implementar estrategias efectivas para reducir la incidencia de siniestros, promoviendo así una cultura de responsabilidad y seguridad en las vías públicas. Este enfoque no solo facilita la toma de decisiones informadas, sino que también fomenta la conciencia colectiva sobre la importancia de la prevención en la reducción de pérdidas humanas y económicas.    """)
##st.markdown("Este proyecto analiza los siniestros nacionales utilizando un conjunto de datos aleatorio. A continuación, se presentan algunos gráficos y análisis basados en los datos disponibles.")
imagen = "imagen1.png"
imagen3 = plt.imread(imagen)
plt.imshow(imagen3)
plt.axis('off')
st.image(imagen3, caption="Análisis de Siniestros", use_column_width=True)

# -----------------------------------------------------------
# CARGA Y PREPARACIÓN DE DATOS
# -----------------------------------------------------------

@st.cache_data
def load_data(path: str = "Siniestros_nacionales_aleatorio_trim6.csv") -> pd.DataFrame:
    df = pd.read_csv(path)

    ##2:03:00